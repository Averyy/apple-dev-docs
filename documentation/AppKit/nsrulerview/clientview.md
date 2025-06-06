# clientView

**Framework**: AppKit  
**Kind**: property

The receiver’s client view, if it has one.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var clientView: NSView? { get set }
```

#### Discussion

`aView` is either the document view of the NSScrollView that contains the receiver or a subview of the document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/clientview)*