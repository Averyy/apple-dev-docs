# imagePadding

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance between the button’s image and text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) CGFloat imagePadding;
```

## Discussion

Use this property to adjust the distance from the title and subtitle. This doesn’t affect the distance to the button’s edge.

## See Also

### Configuring images
- [image](./image.md)
  The foreground image the button displays.
- [imagePlacement](./imageplacement.md)
  The edge against which the button places the image.
- [imageColorTransformer](./imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](./preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/imagepadding)*