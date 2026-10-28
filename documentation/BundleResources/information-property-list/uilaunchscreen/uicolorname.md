# UIColorName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of a color to use as the background color on the launch screen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UIColorName` (Background color)
- **Type**: string

## Discussion

Provide a value for this key that’s the name of a color in your asset catalog. You use the same string for the value that you might use when calling the [`init(named:)`](../../../UIKit/uicolor/init%28named%29.md) initializer of [`UIColor`](../../../UIKit/uicolor.md).

If you don’t set a color, the system uses a default of [`systemBackground`](../../../UIKit/uicolor/systembackground.md), which varies according to whether the user has selected the light appearance or Dark Mode for the device.

## See Also

### Main Interface
- [UIImageName](./uiimagename.md)
  The name of an image to display during app launch.
- [UIImageRespectsSafeAreaInsets](./uiimagerespectssafeareainsets.md)
  A Boolean that specifies whether the launch image should respect the safe area insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen/uicolorname)*