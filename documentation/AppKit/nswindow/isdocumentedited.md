# isDocumentEdited

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window’s document has been edited.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isDocumentEdited: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window’s document has been edited; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). Initially, by default, `NSWindow` objects are in the “not edited” state.

You should set [`isDocumentEdited`](nswindow/isdocumentedited.md) to [`true`](https://developer.apple.com/documentation/Swift/true) every time the window’s document changes in such a way that it needs to be saved. Conversely, when the document is saved, you should set the property to [`true`](https://developer.apple.com/documentation/Swift/true) when the window’s document has been edited; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). Then, before closing the window you can examine the value of the property to determine whether to allow the user a chance to save the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isdocumentedited)*