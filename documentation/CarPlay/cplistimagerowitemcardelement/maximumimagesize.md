# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum dimensions for normal-height images.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumImageSize;
```

## Discussion

When the [`showsImageFullHeight`](./showsimagefullheight.md) property is `false`, this property defines the maximum size for images. When creating images, adjust the size of your image to match the maximum value.

To determine the maximum pixel dimensions for images, multiply the value in this property by the current scale factor for your CarPlay interface. Get the interface scale factor from the traits in the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Getting the expected image dimensions
- [class var maximumFullHeightImageSize: CGSize](./maximumfullheightimagesize.md)
  The maximum dimensions for full-height images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/maximumimagesize)*