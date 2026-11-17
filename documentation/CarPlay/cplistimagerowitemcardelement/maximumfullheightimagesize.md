# maximumFullHeightImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum dimensions for full-height images.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumFullHeightImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumFullHeightImageSize;
```

## Discussion

When the [`showsImageFullHeight`](./showsimagefullheight.md) property is `true`, this property defines the maximum size for images. When creating images, adjust the size of your image to match the maximum value.

To determine the maximum pixel dimensions for images, multiply the value in this property by the current scale factor for your CarPlay interface. Get the interface scale factor from the traits in the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Getting the expected image dimensions
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for normal-height images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/maximumfullheightimagesize)*