# contentViewInsets

**Framework**: TVUIKit  
**Kind**: property

The spacing between the content view and its peer and containing views.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var contentViewInsets: NSDirectionalEdgeInsets { get set }
```

#### Discussion

Use negative values for positive spacing. The [`top`](https://developer.apple.com/documentation/AppKit/NSDirectionalEdgeInsets/top) and [`bottom`](https://developer.apple.com/documentation/AppKit/NSDirectionalEdgeInsets/bottom) values represent the spacing between the content view and the header and footer views, respectively. The [`leading`](https://developer.apple.com/documentation/AppKit/NSDirectionalEdgeInsets/leading) and [`trailing`](https://developer.apple.com/documentation/AppKit/NSDirectionalEdgeInsets/trailing) values represent the spacing between the content view and the lockup view. The default value is [`NSDirectionalEdgeInsetsZero`](https://developer.apple.com/documentation/AppKit/NSDirectionalEdgeInsetsZero).

## See Also

- [var contentSize: CGSize](tvlockupview/contentsize.md)
  The size of the content view.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](tvlockupview/focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentviewinsets)*