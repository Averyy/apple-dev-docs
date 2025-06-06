# constraintsAffectingLayout

**Framework**: AppKit  
**Kind**: property

The constraints that impact the layout of the anchor.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var constraintsAffectingLayout: [NSLayoutConstraint] { get }
```

## See Also

- [var hasAmbiguousLayout: Bool](nslayoutanchor/hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [var name: String](nslayoutanchor/name.md)
  The name assigned to the anchor for debugging purposes.
- [var item: AnyObject?](nslayoutanchor/item.md)
  The layout item used to calculate the anchor’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutanchor/constraintsaffectinglayout)*