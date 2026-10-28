# isDragging

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the receiver is being dragged.

**Availability**:
- macOS

## Declaration

```swift
var isDragging: Bool { get }
```

```objc
@property (readonly, getter=isDragging) BOOL dragging;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver is being dragged, [`false`](../../Swift/false.md) otherwise.

## See Also

### Drawing and event handling
- [func draw(NSRect)](./draw%28_%29.md)
  Draws the receiver’s image that appears in the supplied rectangle.
- [func trackMouse(with: NSEvent, adding: Bool) -> Bool](./trackmouse%28with,adding%29.md)
  Handles user manipulation of the receiver in its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/isdragging)*