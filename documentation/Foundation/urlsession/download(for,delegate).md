# download(for:delegate:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Retrieves the contents of a URL based on the specified URL request and delivers the URL of the saved file asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func download(for request: URLRequest, delegate: (any URLSessionTaskDelegate)? = nil) async throws -> (URL, URLResponse)
```

#### Return Value

An asynchronously-delivered tuple that contains the location of the downloaded file as a URL, and a [`URLResponse`](../urlresponse.md).

## Parameters

- `request`: A URL request object that provides request-specific information such as the URL, cache policy, request type, and body data or body stream.
- `delegate`: A delegate that receives life cycle and authentication challenge callbacks as the transfer progresses.

## See Also

### Performing asynchronous transfers
- [func bytes(for: URLRequest, delegate: (any URLSessionTaskDelegate)?) async throws -> (URLSession.AsyncBytes, URLResponse)](./bytes%28for,delegate%29.md)
  Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [func bytes(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (URLSession.AsyncBytes, URLResponse)](./bytes%28from,delegate%29.md)
  Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [URLSession.AsyncBytes](./asyncbytes.md)
  An asynchronous sequence of bytes.
- [func data(for: URLRequest, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](./data%28for,delegate%29.md)
  Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.
- [func data(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](./data%28from,delegate%29.md)
  Retrieves the contents of a URL and delivers the data asynchronously.
- [func data(for: URLRequest) async throws -> (Data, URLResponse)](./data%28for%29.md)
  Convenience method to load data using a URLRequest, creates and resumes a URLSessionDataTask internally.
- [func data(from: URL) async throws -> (Data, URLResponse)](./data%28from%29.md)
  Convenience method to load data using a URL, creates and resumes a URLSessionDataTask internally.
- [func download(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (URL, URLResponse)](./download%28from,delegate%29.md)
  Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.
- [func download(resumeFrom: Data, delegate: (any URLSessionTaskDelegate)?) async throws -> (URL, URLResponse)](./download%28resumefrom,delegate%29.md)
  Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [func upload(for: URLRequest, from: Data, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](./upload%28for,from,delegate%29.md)
  Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [func upload(for: URLRequest, fromFile: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](./upload%28for,fromfile,delegate%29.md)
  Uploads data to a URL and delivers the result asynchronously.
- [func upload(for: URLRequest, from: Data) async throws -> (Data, URLResponse)](./upload%28for,from%29.md)
  Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [func upload(for: URLRequest, fromFile: URL) async throws -> (Data, URLResponse)](./upload%28for,fromfile%29.md)
  Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [protocol URLSessionTaskDelegate](../urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/download(for:delegate:))*