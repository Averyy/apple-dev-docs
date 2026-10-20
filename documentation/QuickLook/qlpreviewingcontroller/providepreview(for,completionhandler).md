# providePreview(for:completionHandler:)

**Framework**: Quick Look  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func providePreview(for request: QLFilePreviewRequest) async throws -> QLPreviewReply
```

#### Discussion

Use this method to provide a QLPreviewReply that provides preview in the form of NSData, NSURL, PDFDocument, or a drawing into a context.

## Parameters

- `request`: An object which contains information about the preview that should be provided. It contains the URL of the file to provide a preview for.
- `handler`: Call the completion handler with a QLPreviewReply if you can provide a preview, or with an NSError if you cannot. If an error is passed or reply is nil, a generic preview will be provided instead. The handler can be called asynchronously after the method has returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewingcontroller/providepreview(for:completionhandler:))*