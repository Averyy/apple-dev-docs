# maskedContentView

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The content view in focus.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var maskedContentView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * maskedContentView;
```

#### Discussion

Use this property to modify the parallax effect applied on the cell and its content. Add any other UI elements to be included on the cell to this view.

This view fills the entire screen.

## See Also

### Accessing Cell Views
- [var maskedBackgroundView: UIView](./maskedbackgroundview.md)
  The background view that performs the parallax effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/maskedcontentview)*