# accessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s accessory view to `aView`.

**Availability**:
- macOS

## Declaration

```swift
var accessoryView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * accessoryView;
```

#### Discussion

Raises an `NSInternalInconsistencyException` if `aView` is not `nil` and the receiver has no client view.

## See Also

### Related Documentation
- [var reservedThicknessForAccessoryView: CGFloat](./reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/accessoryview)*