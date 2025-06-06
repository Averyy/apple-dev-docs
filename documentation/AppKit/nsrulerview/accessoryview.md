# accessoryView

**Framework**: AppKit  
**Kind**: property

The receiver’s accessory view to `aView`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var accessoryView: NSView? { get set }
```

#### Discussion

Raises an `NSInternalInconsistencyException` if `aView` is not `nil` and the receiver has no client view.

## See Also

- [var reservedThicknessForAccessoryView: CGFloat](nsrulerview/reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/accessoryview)*