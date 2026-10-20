# contentView

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The main view for the lockup.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var contentView: UIView { get }
```

```objc
@property (nonatomic, strong, readonly) UIView * contentView;
```

#### Discussion

Add subviews to the `contentView`. Don’t add views direcly to the lockup view.

## See Also

### Adding subviews
- [var headerView: TVLockupHeaderFooterView?](./headerview.md)
  A view containing header information.
- [var footerView: TVLockupHeaderFooterView?](./footerview.md)
  A view containing footer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentview)*