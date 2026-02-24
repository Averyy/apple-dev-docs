# setDocumentEdited(_:)

**Framework**: AppKit  
**Kind**: method

Sets the document edited flag for the window controller.

**Availability**:
- macOS ?+

## Declaration

```swift
func setDocumentEdited(_ dirtyFlag: Bool)
```

#### Discussion

The window controller uses this flag to control whether its associated window shows up as dirty. You should not call this method directly for window controllers with an associated document; the document calls this method on its window controllers as needed.

## Parameters

- `dirtyFlag`: [`true`](https://developer.apple.com/documentation/Swift/true) if the document has been edited since its last save, [`false`](https://developer.apple.com/documentation/Swift/false) if it hasn’t.

## See Also

- [var document: AnyObject?](nswindowcontroller/document.md)
  The document associated with the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/setdocumentedited(_:))*