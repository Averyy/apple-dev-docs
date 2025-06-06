# Uploading data to a website

**Framework**: Foundation

Post data from your app to servers.

#### Overview

Many apps work with servers that accept uploads of files like images or documents, or use web service API endpoints that accept structured data like JSON. To upload data from your app, you use a [`URLSession`](urlsession.md) instance to create a [`URLSessionUploadTask`](urlsessionuploadtask.md) instance. The upload task uses a [`URLRequest`](urlrequest.md) instance that details how the upload is to be performed.

##### Prepare Your Data for Upload

The data to upload can be the contents of a file, a stream, or data, as is the case in the following example.

Many web service endpoints take JSON-formatted data, which you create by using the  [`JSONEncoder`](jsonencoder.md) class on [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable) types like arrays and dictionaries. As shown in the following example, you can declare a structure that conforms to [`Codable`](https://developer.apple.com/documentation/Swift/Codable), create an instance of this type, and use [`JSONEncoder`](jsonencoder.md) to encode the instance to JSON data for upload.

Preparing JSON data for upload

```swift
struct Order: Codable {
    let customerId: String
    let items: [String]
}

// ...

let order = Order(customerId: "12345",
                  items: ["Cheese pizza", "Diet soda"])
guard let uploadData = try? JSONEncoder().encode(order) else {
    return
}
```

There are many other ways to create a data instance, such as encoding an image as JPEG or PNG data, or converting a string to data by using an encoding like UTF-8.

##### Configure an Upload Request

An upload task requires a [`URLRequest`](urlrequest.md) instance. As shown in the following example, set the [`httpMethod`](urlrequest/httpmethod.md) property of the request to `"``POST``"` or `"PUT"`, depending on what the server supports and expects. Use the [`setValue(_:forHTTPHeaderField:)`](urlrequest/setvalue(_:forhttpheaderfield:).md) method to set the values of any HTTP headers that you want to provide, except the `Content-Length` header. The session figures out content length automatically from the size of your data.

Configuring a URL request

```swift
let url = URL(string: "https://example.com/post")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
```

##### Create and Start an Upload Task

To begin an upload, call [`uploadTask(with:from:completionHandler:)`](urlsession/uploadtask(with:from:completionhandler:).md) on a [`URLSession`](urlsession.md) instance to create an uploading [`URLSessionTask`](urlsessiontask.md) instance, passing in the request and the data instances you’ve previously set up. Because tasks start in a suspended state, you begin the network loading process by calling [`resume()`](urlsessiontask/resume().md) on the task. The following example uses the shared `URLSession` instance, and receives its results in a completion handler. The handler checks for transport and server errors before using any returned data.

Starting an upload task

```swift
let task = URLSession.shared.uploadTask(with: request, from: uploadData) { data, response, error in
    if let error = error {
        print ("error: \(error)")
        return
    }
    guard let response = response as? HTTPURLResponse,
        (200...299).contains(response.statusCode) else {
        print ("server error")
        return
    }
    if let mimeType = response.mimeType,
        mimeType == "application/json",
        let data = data,
        let dataString = String(data: data, encoding: .utf8) {
        print ("got data: \(dataString)")
    }
}
task.resume()
```

##### Alternatively Upload By Setting a Delegate

As an alternative to the completion handler approach, you can instead set a delegate on a session you configure, and then create the upload task with [`uploadTask(with:from:)`](urlsession/uploadtask(with:from:).md). In this scenario, you implement methods from the [`URLSessionDelegate`](urlsessiondelegate.md) and [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md) protocols. These methods receive the server response and any data or transport errors.

## See Also

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [Uploading streams of data](uploading-streams-of-data.md)
  Send a stream of data to a server.
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)
  Pause and resume an upload without starting over, even when the connection is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uploading-data-to-a-website)*