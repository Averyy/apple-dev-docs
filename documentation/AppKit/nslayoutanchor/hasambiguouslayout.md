# hasAmbiguousLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var hasAmbiguousLayout: Bool { get }
```

```objc
@property (readonly) BOOL hasAmbiguousLayout;
```

## See Also

### Debugging the anchor
- [var constraintsAffectingLayout: [NSLayoutConstraint]](./constraintsaffectinglayout.md)
  The constraints that impact the layout of the anchor.
- [var name: String](./name.md)
  The name assigned to the anchor for debugging purposes.
- [var item: AnyObject?](./item.md)
  The layout item used to calculate the anchor’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/hasambiguouslayout)*