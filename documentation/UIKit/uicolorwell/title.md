# title

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The title for the color picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

#### Discussion

Use this property to explain what kind of color to pick, like “Stroke Color” or “Fill Color”.

## See Also

### Configuring color picker attributes
- [var maximumLinearExposure: CGFloat](./maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color well.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.
- [var supportsEyedropper: Bool](./supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color well.
- [var selectedColor: UIColor?](./selectedcolor.md)
  The selected color in the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorwell/title)*