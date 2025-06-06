# QLPreviewingController

**Framework**: Quick Look UI  
**Kind**: protocol

A protocol for implementing a custom controller to create previews of files.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol QLPreviewingController : NSObjectProtocol
```

#### Overview

A controller that implements the `QLPreviewingController` protocol must at least implement [`preparePreviewOfSearchableItem(identifier:queryString:completionHandler:)`](qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:).md) or [`preparePreviewOfFile(at:completionHandler:)`](qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:).md).

## Topics

### Instance Methods
- [func preparePreviewOfFile(at: URL, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:).md)
  Prepares the preview of a file at the specified file’s URL.
- [func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler: ((any Error)?) -> Void)](qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:).md)
  Prepares the preview for a file by using the data from Spotlight’s searchable item.
- [func providePreview(for: QLFilePreviewRequest, completionHandler: (QLPreviewReply?, (any Error)?) -> Void)](qlpreviewingcontroller/providepreview(for:completionhandler:).md)
  Prepares the preview of a file identified within a file preview request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller)*