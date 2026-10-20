# maskedBackgroundView

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The background view that performs the parallax effect.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var maskedBackgroundView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * maskedBackgroundView;
```

#### Discussion

The `maskedBackgroundView` property returns the current cell’s background view. Modify properties of this view to customize the parallax effect. Generally, you should add an opaque image to the view.

## See Also

### Accessing Cell Views
- [var maskedContentView: UIView](./maskedcontentview.md)
  The content view in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/maskedbackgroundview)*