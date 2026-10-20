# isDocumentEdited

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window’s document has been edited.

**Availability**:
- macOS

## Declaration

```swift
var isDocumentEdited: Bool { get set }
```

```objc
@property (getter=isDocumentEdited) BOOL documentEdited;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window’s document has been edited; otherwise, [`false`](../../Swift/false.md). Initially, by default, `NSWindow` objects are in the “not edited” state.

You should set [`isDocumentEdited`](./isdocumentedited.md) to [`true`](../../Swift/true.md) every time the window’s document changes in such a way that it needs to be saved. Conversely, when the document is saved, you should set the property to [`true`](../../Swift/true.md) when the window’s document has been edited; otherwise, [`false`](../../Swift/false.md). Then, before closing the window you can examine the value of the property to determine whether to allow the user a chance to save the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isdocumentedited)*