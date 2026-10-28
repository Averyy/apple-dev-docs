# contentSize

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The size of the content view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var contentSize: CGSize { get set }
```

```objc
@property (nonatomic, assign) CGSize contentSize;
```

## Discussion

Use this property to explicitly set the size of the content view. If [`frame`](../../UIKit/uiview/frame.md) is explicitly set, it takes precedence over `contentSize`.

## See Also

### Setting view size
- [var contentViewInsets: NSDirectionalEdgeInsets](./contentviewinsets.md)
  The spacing between the content view and its peer and containing views.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](./focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentsize)*