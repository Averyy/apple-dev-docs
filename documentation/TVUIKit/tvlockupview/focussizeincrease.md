# focusSizeIncrease

**Framework**: TVUIKit  
**Kind**: property

The inset or outset values specifying your content’s size increase when in focus.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var focusSizeIncrease: NSDirectionalEdgeInsets { get set }
```

#### Discussion

Use negative values for a size increase. The values contribute to the lockup view’s intrinsic content size and guide layout update when focus state changes.

## See Also

- [var contentSize: CGSize](tvlockupview/contentsize.md)
  The size of the content view.
- [var contentViewInsets: NSDirectionalEdgeInsets](tvlockupview/contentviewinsets.md)
  The spacing between the content view and its peer and containing views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/focussizeincrease)*