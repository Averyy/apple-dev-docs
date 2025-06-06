# contentView

**Framework**: TVUIKit  
**Kind**: property

The main view for the lockup.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var contentView: UIView { get }
```

#### Discussion

Add subviews to the `contentView`. Don’t add views direcly to the lockup view.

## See Also

- [var headerView: TVLockupHeaderFooterView?](tvlockupview/headerview.md)
  A view containing header information.
- [var footerView: TVLockupHeaderFooterView?](tvlockupview/footerview.md)
  A view containing footer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/contentview)*