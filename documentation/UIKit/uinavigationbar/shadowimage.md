# shadowImage

**Framework**: UIKit  
**Kind**: property

The shadow image to be used for the navigation bar.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shadowImage: UIImage? { get set }
```

#### Discussion

The default value is `nil`, which corresponds to the default shadow image. When non-`nil`, this property represents a custom shadow image to show instead of the default. To show a custom shadow image, you must also set a custom background image with the [`setBackgroundImage(_:for:)`](uinavigationbar/setbackgroundimage(_:for:).md) method. If the default background image is used, then the default shadow image is used regardless of the value of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/shadowimage)*