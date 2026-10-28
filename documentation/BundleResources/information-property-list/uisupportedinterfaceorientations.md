# UISupportedInterfaceOrientations

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The interface orientations supported by your app.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+

## Details

- **Name**: `UISupportedInterfaceOrientations` (Supported interface orientations)
- **Type**: array of string 

## Possible Values

- `UIInterfaceOrientationPortrait`: The app supports the display in portrait mode, with the device upright and the front camera at the top.
- `UIInterfaceOrientationPortraitUpsideDown`: The app supports the display in portrait mode but is upside down, with the device upright and  the front camera at the bottom. [`UIViewController`](../../UIKit/uiviewcontroller.md) ignores this option on devices without a Home button.
- `UIInterfaceOrientationLandscapeLeft`: The app supports the display in landscape mode, with the device upright and the front camera on the right.
- `UIInterfaceOrientationLandscapeRight`: The app supports the display in landscape mode, with the device upright and the front camera on the left.



**Default**: `UIInterfaceOrientationPortrait`

## Discussion

> 💡 **Tip**: To set supported orientations for specific platforms and devices, add platform- or device-specific keys to the information property list. For more information, see [Add platform- and device-specific properties](../managing-your-app-s-information-property-list.md#Add-platform-and-device-specific-properties).

## See Also

### Orientation
- [UIInterfaceOrientation](./uiinterfaceorientation.md)
  The initial orientation of the app’s user interface.
- [UIPreferredDefaultInterfaceOrientation](./uipreferreddefaultinterfaceorientation.md)
  A string that indicates the preferred initial interface orientation for iPad and iPhone apps running on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportedinterfaceorientations)*