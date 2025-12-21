# overlayContentView

**Framework**: UIKit  
**Kind**: property

A view for hosting layered content on top of the image view.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
var overlayContentView: UIView { get }
```

#### Discussion

Use this view to host content that you want layered on top of the image view. This view is managed by the image view itself and is automatically sized to fill the image view’s frame rectangle. Add your subviews and use layout constraints to position them within the view. When the [`adjustsImageWhenAncestorFocused`](uiimageview/adjustsimagewhenancestorfocused.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the overlay view receives the same floating effects as the image view when it’s focused.

The view in this property clips its subviews to its bounds rectangle by default, but you can change that behavior using the [`clipsToBounds`](uiview/clipstobounds.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/overlaycontentview)*