# requestDocument(_:)

**Framework**: Proximityreader  
**Kind**: method

Presents a sheet to read a mobile document and returns the relevant response.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
@discardableResult
final func requestDocument<Request>(_ request: Request) async throws -> Request.Response where Request : MobileDocumentRequest
```

## Mentions

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)

#### Return Value

A [`Response`](mobiledocumentrequest/response.md) if the request was successful.

#### Discussion

Call this method to begin requesting data contained in a mobile document. This method displays a system-provided sheet with instructions on what the mobile document holder needs to do. This UI remains onscreen until the system reads the person’s mobile document, you cancel the task, or an error occurs.

> **Note**: This method throws a [`MobileDocumentReaderError`](mobiledocumentreadererror.md) if a mobile document request error occurs.

## Parameters

- `request`: The mobile document request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadersession/requestdocument(_:))*