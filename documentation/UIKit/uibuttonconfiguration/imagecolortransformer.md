# imageColorTransformer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A block that transforms the image color when the button state changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) UIConfigurationColorTransformer imageColorTransformer;
```

#### Discussion

Use this property to transform an image to, for example, a monochrome or tinted image.

## See Also

### Configuring images
- [image](./image.md)
  The foreground image the button displays.
- [imagePadding](./imagepadding.md)
  The distance between the button’s image and text.
- [imagePlacement](./imageplacement.md)
  The edge against which the button places the image.
- [preferredSymbolConfigurationForImage](./preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/imagecolortransformer)*