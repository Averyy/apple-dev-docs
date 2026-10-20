# shadowImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The shadow image to be used for the navigation bar.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shadowImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * shadowImage;
```

#### Discussion

The default value is `nil`, which corresponds to the default shadow image. When non-`nil`, this property represents a custom shadow image to show instead of the default. To show a custom shadow image, you must also set a custom background image with the [`setBackgroundImage(_:for:)`](./setbackgroundimage%28_,for%29.md) method. If the default background image is used, then the default shadow image is used regardless of the value of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/shadowimage)*