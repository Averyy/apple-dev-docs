# contentViewInsets

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The spacing between the content view and its peer and containing views.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var contentViewInsets: NSDirectionalEdgeInsets { get set }
```

```objc
@property (nonatomic, assign) NSDirectionalEdgeInsets contentViewInsets;
```

## Discussion

Use negative values for positive spacing. The [`top`](../../AppKit/nsdirectionaledgeinsets/top.md) and [`bottom`](../../AppKit/nsdirectionaledgeinsets/bottom.md) values represent the spacing between the content view and the header and footer views, respectively. The [`leading`](../../AppKit/nsdirectionaledgeinsets/leading.md) and [`trailing`](../../AppKit/nsdirectionaledgeinsets/trailing.md) values represent the spacing between the content view and the lockup view. The default value is [`NSDirectionalEdgeInsetsZero`](../../AppKit/nsdirectionaledgeinsetszero.md).

## See Also

### Setting view size
- [var contentSize: CGSize](./contentsize.md)
  The size of the content view.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](./focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentviewinsets)*