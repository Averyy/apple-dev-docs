# item

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout item used to calculate the anchor’s position.

**Availability**:
- macOS 10.12+

## Declaration

```swift
weak var item: AnyObject? { get }
```

```objc
@property (weak, readonly, nullable) id item;
```

## See Also

### Debugging the anchor
- [var constraintsAffectingLayout: [NSLayoutConstraint]](./constraintsaffectinglayout.md)
  The constraints that impact the layout of the anchor.
- [var hasAmbiguousLayout: Bool](./hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [var name: String](./name.md)
  The name assigned to the anchor for debugging purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/item)*