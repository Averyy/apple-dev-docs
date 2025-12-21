# isHorizontalContentSizeConstraintActive

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the view’s horizontal size constraints are active.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var isHorizontalContentSizeConstraintActive: Bool { get set }
```

#### Discussion

Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) lets Auto Layout optimize layout operations by ignoring the view’s intrinsic content size. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which causes the system to take the view’s content size into account.

## See Also

- [var isVerticalContentSizeConstraintActive: Bool](nsview/isverticalcontentsizeconstraintactive.md)
  A Boolean value that indicates whether the view’s vertical size constraints are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/ishorizontalcontentsizeconstraintactive)*