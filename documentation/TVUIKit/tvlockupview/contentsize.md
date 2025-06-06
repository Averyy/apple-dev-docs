# contentSize

**Framework**: TVUIKit  
**Kind**: property

The size of the content view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var contentSize: CGSize { get set }
```

#### Discussion

Use this property to explicitly set the size of the content view. If [`frame`](https://developer.apple.com/documentation/UIKit/UIView/frame) is explicitly set, it takes precedence over `contentSize`.

## See Also

- [var contentViewInsets: NSDirectionalEdgeInsets](tvlockupview/contentviewinsets.md)
  The spacing between the content view and its peer and containing views.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](tvlockupview/focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentsize)*