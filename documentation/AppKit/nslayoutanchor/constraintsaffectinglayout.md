# constraintsAffectingLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The constraints that impact the layout of the anchor.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var constraintsAffectingLayout: [NSLayoutConstraint] { get }
```

```objc
@property (readonly) NSArray<NSLayoutConstraint *> * constraintsAffectingLayout;
```

## See Also

### Debugging the anchor
- [var hasAmbiguousLayout: Bool](./hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [var name: String](./name.md)
  The name assigned to the anchor for debugging purposes.
- [var item: AnyObject?](./item.md)
  The layout item used to calculate the anchor’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/constraintsaffectinglayout)*