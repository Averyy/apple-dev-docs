# clientView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s client view, if it has one.

**Availability**:
- macOS

## Declaration

```swift
weak var clientView: NSView? { get set }
```

```objc
@property (weak, nullable) NSView * clientView;
```

## Discussion

`aView` is either the document view of the NSScrollView that contains the receiver or a subview of the document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/clientview)*