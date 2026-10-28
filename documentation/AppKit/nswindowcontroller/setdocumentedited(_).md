# setDocumentEdited(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the document edited flag for the window controller.

**Availability**:
- macOS

## Declaration

```swift
func setDocumentEdited(_ dirtyFlag: Bool)
```

```objc
- (void) setDocumentEdited:(BOOL) dirtyFlag;
```

## Discussion

The window controller uses this flag to control whether its associated window shows up as dirty. You should not call this method directly for window controllers with an associated document; the document calls this method on its window controllers as needed.

## Parameters

- `dirtyFlag`: [`true`](../../Swift/true.md) if the document has been edited since its last save, [`false`](../../Swift/false.md) if it hasn’t.

## See Also

### Accessing the Document
- [var document: AnyObject?](./document.md)
  The document associated with the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/setdocumentedited(_:))*