# URLSession.AsyncBytes

**Framework**: Foundation  
**Kind**: struct

An asynchronous sequence of bytes.

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
struct AsyncBytes
```

## Topics

### Adapting textual sequences
- [struct AsyncCharacterSequence](asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct AsyncLineSequence](asynclinesequence.md)
  An asynchronous sequence of lines of text.
### Accessing the URL session task
- [var task: URLSessionDataTask](urlsession/asyncbytes/task.md)
  The URL session task that performs the data transfer.
### Structures
- [URLSession.AsyncBytes.Iterator](urlsession/asyncbytes/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func bytes(for: URLRequest, delegate: (any URLSessionTaskDelegate)?) async throws -> (URLSession.AsyncBytes, URLResponse)](urlsession/bytes(for:delegate:).md)
  Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [func bytes(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (URLSession.AsyncBytes, URLResponse)](urlsession/bytes(from:delegate:).md)
  Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [func data(for: URLRequest, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](urlsession/data(for:delegate:).md)
  Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.
- [func data(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](urlsession/data(from:delegate:).md)
  Retrieves the contents of a URL and delivers the data asynchronously.
- [func data(for: URLRequest) async throws -> (Data, URLResponse)](urlsession/data(for:).md)
  Convenience method to load data using a URLRequest, creates and resumes a URLSessionDataTask internally.
- [func data(from: URL) async throws -> (Data, URLResponse)](urlsession/data(from:).md)
  Convenience method to load data using a URL, creates and resumes a URLSessionDataTask internally.
- [func download(for: URLRequest, delegate: (any URLSessionTaskDelegate)?) async throws -> (URL, URLResponse)](urlsession/download(for:delegate:).md)
  Retrieves the contents of a URL based on the specified URL request and delivers the URL of the saved file asynchronously.
- [func download(from: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (URL, URLResponse)](urlsession/download(from:delegate:).md)
  Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.
- [func download(resumeFrom: Data, delegate: (any URLSessionTaskDelegate)?) async throws -> (URL, URLResponse)](urlsession/download(resumefrom:delegate:).md)
  Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [func upload(for: URLRequest, from: Data, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](urlsession/upload(for:from:delegate:).md)
  Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [func upload(for: URLRequest, fromFile: URL, delegate: (any URLSessionTaskDelegate)?) async throws -> (Data, URLResponse)](urlsession/upload(for:fromfile:delegate:).md)
  Uploads data to a URL and delivers the result asynchronously.
- [func upload(for: URLRequest, from: Data) async throws -> (Data, URLResponse)](urlsession/upload(for:from:).md)
  Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [func upload(for: URLRequest, fromFile: URL) async throws -> (Data, URLResponse)](urlsession/upload(for:fromfile:).md)
  Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [protocol URLSessionTaskDelegate](urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/asyncbytes)*