# beginSheet(with:modalFor:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents a document-modal PDF panel.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func beginSheet(with pdfInfo: NSPDFInfo, modalFor docWindow: NSWindow?) async -> Int
```

#### Discussion

This method presents a slightly different PDF panel depending on whether the [`requestsParentDirectory`](nspdfpanel/options-swift.struct/requestsparentdirectory.md) constant is set. If the user dismisses the panel without canceling it, this method updates the [`NSPDFInfo`](nspdfinfo.md) object with any changes the user makes.

## Parameters

- `pdfInfo`: The   object describing the parameters to be used when creating the PDF file.
- `docWindow`: The window in which the PDF panel will be presented.
- `completionHandler`: The block called when the user dismisses the PDF panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/beginsheet(with:modalfor:completionhandler:))*