# Fetching website data into memory

**Framework**: Foundation

Receive data directly into memory by creating a data task from a URL session.

#### Overview

For small interactions with remote servers, you can use the [`URLSessionDataTask`](urlsessiondatatask.md) class to receive response data into memory (as opposed to using the [`URLSessionDownloadTask`](urlsessiondownloadtask.md) class, which stores the data directly to the file system). A data task is ideal for uses like calling a web service endpoint.

You use a URL session instance to create the task. If your needs are fairly simple, you can use the [`shared`](urlsession/shared.md) instance of the [`URLSession`](urlsession.md) class. If you want to interact with the transfer through delegate callbacks, you’ll need to create a session instead of using the shared instance. You use a [`URLSessionConfiguration`](urlsessionconfiguration.md) instance when creating a session, also passing in a class that implements [`URLSessionDelegate`](urlsessiondelegate.md) or one of its subprotocols. Sessions can be reused to create multiple tasks, so for each unique configuration you need, create a session and store it as a property.

> **Note**:  Be careful to not create more sessions than you need. For example, if you have several parts of your app that need a similarly configured session, create one session and share it among them.

Once you have a session, you create a data task with one of the `dataTask()` methods. Tasks are created in a suspended state, and can be started by calling [`resume()`](urlsessiontask/resume().md).

##### Receive Results with a Completion Handler

The simplest way to fetch data is to create a data task that uses a completion handler. With this arrangement, the task delivers the server’s response, data, and possibly errors to a completion handler block that you provide.  shows the relationship between a session and a task, and how results are delivered to the completion handler.

![Figure showing a URL Session creating a URL Session Data Task. The task then sends the original request, retrieved data, or an error to the completion handler.](https://docs-assets.developer.apple.com/published/f72e1228818d684018a52c23000f322b/media-4332611%402x.png)

To create a data task that uses a completion handler, call the [`dataTask(with:)`](urlsession/datatask(with:)-10dy7.md) method of `URLSession`. Your completion handler needs to do three things:

1. Verify that the `error` parameter is `nil`. If not, a transport error has occurred; handle the error and exit.
2. Check the `response` parameter to verify that the status code indicates success and that the MIME type is an expected value. If not, handle the server error and exit.
3. Use the `data` instance as needed.

The following example shows a `startLoad()` method for fetching a URL’s contents. It starts by using the [`URLSession`](urlsession.md) class’s shared instance to create a data task that delivers its results to a completion handler. After checking for local and server errors, this handler converts the data to a string, and uses it to populate a `WKWebView` outlet. Of course, your app might have other uses for fetched data, like parsing it into a data model.

Creating a completion handler to receive data-loading results

```swift
func startLoad() {
    let url = URL(string: "https://www.example.com/")!
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error {
            self.handleClientError(error)
            return
        }
        guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
            self.handleServerError(response)
            return
        }
        if let mimeType = httpResponse.mimeType, mimeType == "text/html",
            let data = data,
            let string = String(data: data, encoding: .utf8) {
            DispatchQueue.main.async {
                self.webView.loadHTMLString(string, baseURL: url)
            }
        }
    }
    task.resume()
}

```

> ❗ **Important**:  The completion handler is called on a different Grand Central Dispatch queue than the one that created the task. Therefore, any work that uses `data` or `error` to update the UI — like updating `webView` — should be explicitly placed on the main queue, as shown here.

##### Receive Transfer Details and Results with a Delegate

For a greater level of access to the task’s activity as it proceeds, when creating the data task, you can set a delegate on the session, rather than providing a completion handler.  shows this arrangement.

![Figure showing a URLSession creating a URLSessionDataTask. The session calls back to the delegate with progress updates, retrieved data, authentication challenges, and other events.](https://docs-assets.developer.apple.com/published/0c1059a51359f7d0cb68b8feba1785f7/media-4332610%402x.png)

With this approach, portions of the data are provided to the [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) method of [`URLSessionDataDelegate`](urlsessiondatadelegate.md) as they arrive, until the transfer finishes or fails with an error. The delegate also receives other kinds of events as the transfer proceeds.

You need to create your own `URLSession` instance when using the delegate approach, rather than using the `URLSession` class’s simple `shared` instance. Creating a new session allows you to set your own class as the session’s delegate, as shown in the following example.

Declare that your class implements one or more of the delegate protocols ([`URLSessionDelegate`](urlsessiondelegate.md), [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md), [`URLSessionDataDelegate`](urlsessiondatadelegate.md), and [`URLSessionDownloadDelegate`](urlsessiondownloaddelegate.md)). Then create the URL session instance with the initializer [`init(configuration:delegate:delegateQueue:)`](urlsession/init(configuration:delegate:delegatequeue:).md). You can customize the configuration instance used with this initializer. For example, it’s a good idea to set [`waitsForConnectivity`](urlsessionconfiguration/waitsforconnectivity.md) to [`true`](https://developer.apple.com/documentation/swift/true). That way, the session waits for suitable connectivity, rather than failing immediately if the required connectivity is unavailable.

Creating a URLSession that uses a delegate

```swift
private lazy var session: URLSession = {
    let configuration = URLSessionConfiguration.default
    configuration.waitsForConnectivity = true
    return URLSession(configuration: configuration,
                      delegate: self, delegateQueue: nil)
}()
```

The following example shows a `startLoad()` method that uses this session to start a data task, and uses delegate callbacks to handle received data and errors.  This listing implements three delegate callbacks:

- [`urlSession(_:dataTask:didReceive:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md) verifies that the response has a succesful HTTP status code, and that the MIME type is `text/html` or `text/plain`. If either of these is not the case, the task is canceled; otherwise, it’s allowed to proceed.
- [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) takes each `Data` instance received by the task and appends it to a buffer called `receivedData`.
- [`urlSession(_:task:didCompleteWithError:)`](urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:).md) first looks to see if a transport-level error has occurred. If there is no error, it attempts to convert the `receivedData` buffer to a string and set it as the contents of `webView`.

Using a delegate with a URL session data task

```swift
var receivedData: Data?

func startLoad() {
    loadButton.isEnabled = false
    let url = URL(string: "https://www.example.com/")!
    receivedData = Data()
    let task = session.dataTask(with: url)
    task.resume()
}

// delegate methods

func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse,
                completionHandler: @escaping (URLSession.ResponseDisposition) -> Void) {
    guard let response = response as? HTTPURLResponse,
        (200...299).contains(response.statusCode),
        let mimeType = response.mimeType,
        mimeType == "text/html" else {
        completionHandler(.cancel)
        return
    }
    completionHandler(.allow)
}

func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive data: Data) {
    self.receivedData?.append(data)
}

func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: Error?) {
    DispatchQueue.main.async {
        self.loadButton.isEnabled = true
        if let error = error {
            handleClientError(error)
        } else if let receivedData = self.receivedData,
            let string = String(data: receivedData, encoding: .utf8) {
            self.webView.loadHTMLString(string, baseURL: task.currentRequest?.url)
        }
    }
}
```

The various delegate protocols offer methods beyond those shown in the above code, for handling authentication challenges, following redirects, and other special cases. `Using a URL Session`, in the `URLSession` discussion, describes the various callbacks that may occur during a transfer.

## See Also

- [Analyzing HTTP traffic with Instruments](analyzing-http-traffic-with-instruments.md)
  Measure HTTP-based network performance and usage of your apps.
- [class URLSession](urlsession.md)
  An object that coordinates a group of related, network data transfer tasks.
- [class URLSessionTask](urlsessiontask.md)
  A task, like downloading a specific resource, performed in a URL session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/fetching-website-data-into-memory)*