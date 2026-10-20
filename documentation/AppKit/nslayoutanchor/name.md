# name

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name assigned to the anchor for debugging purposes.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var name: String { get }
```

```objc
@property (copy, readonly) NSString * name;
```

## See Also

### Debugging the anchor
- [var constraintsAffectingLayout: [NSLayoutConstraint]](./constraintsaffectinglayout.md)
  The constraints that impact the layout of the anchor.
- [var hasAmbiguousLayout: Bool](./hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [var item: AnyObject?](./item.md)
  The layout item used to calculate the anchor’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/name)*