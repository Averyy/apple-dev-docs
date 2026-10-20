# focusSizeIncrease

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The inset or outset values specifying your content’s size increase when in focus.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var focusSizeIncrease: NSDirectionalEdgeInsets { get set }
```

```objc
@property (nonatomic, assign) NSDirectionalEdgeInsets focusSizeIncrease;
```

#### Discussion

Use negative values for a size increase. The values contribute to the lockup view’s intrinsic content size and guide layout update when focus state changes.

## See Also

### Setting view size
- [var contentSize: CGSize](./contentsize.md)
  The size of the content view.
- [var contentViewInsets: NSDirectionalEdgeInsets](./contentviewinsets.md)
  The spacing between the content view and its peer and containing views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview/focussizeincrease)*