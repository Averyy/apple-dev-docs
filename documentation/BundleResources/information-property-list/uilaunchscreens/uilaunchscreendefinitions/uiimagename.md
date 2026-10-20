# UIImageName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of an image to display during app launch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UIImageName`
- **Type**: string

#### Discussion

Provide a value for this key that’s the name of an image in your asset catalog. You use the same string for the value that you might use when calling the [`init(named:)`](../../../../UIKit/uiimage/init%28named%29.md) initializer of [`UIImage`](../../../../UIKit/uiimage.md). Because the image comes from your asset catalog, you can use slicing to provide a small image that works on many different platforms.

If you don’t specify an image, the display shows the background color, as given by the [`UIColorName`](./uicolorname.md) key. The background color may also show through any transparency in your image.

## See Also

### Main Interface
- [UIColorName](./uicolorname.md)
  The name of a color to use as the background color on the launch screen.
- [UIImageRespectsSafeAreaInsets](./uiimagerespectssafeareainsets.md)
  A Boolean that specifies whether the launch image should respect the safe area insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens/uilaunchscreendefinitions/uiimagename)*