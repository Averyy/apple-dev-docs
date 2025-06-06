# Building a resumable upload server with SwiftNIO

**Framework**: Foundation

Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10006: [`Build robust and resumable file transfers`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10006/).

##### Configure the Sample Code Project

Before you run the sample code project:

1. In the `Package.swift` file of an existing HTTP server project, add `.package(path: "/path/to/swift-nio-resumable-upload")` as one of the dependencies.
2. Import `NIOResumableUpload` in your SwiftNIO bootstrapping code.
3. Create an upload context: `let uploadContext = HTTPResumableUploadContext(origin: "https://example.com")`.
4. Wrap your HTTP server channel handler within `HTTPResumableUploadHandler`.

## See Also

- [Uploading data to a website](uploading-data-to-a-website.md)
  Post data from your app to servers.
- [Uploading streams of data](uploading-streams-of-data.md)
  Send a stream of data to a server.
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)
  Pause and resume an upload without starting over, even when the connection is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio)*