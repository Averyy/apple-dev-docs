# isVerticalContentSizeConstraintActive

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view’s vertical size constraints are active.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isVerticalContentSizeConstraintActive: Bool { get set }
```

```objc
@property (getter=isVerticalContentSizeConstraintActive) BOOL verticalContentSizeConstraintActive;
```

#### Discussion

Setting this property to [`false`](../../Swift/false.md) lets Auto Layout optimize layout operations by ignoring the view’s intrinsic content size. The default value of this property is [`true`](../../Swift/true.md), which causes the system to take the view’s content size into account.

## See Also

### Enabling and Disabling Constraints
- [var isHorizontalContentSizeConstraintActive: Bool](./ishorizontalcontentsizeconstraintactive.md)
  A Boolean value that indicates whether the view’s horizontal size constraints are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isverticalcontentsizeconstraintactive)*