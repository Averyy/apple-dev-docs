# UIInterfaceOrientation

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The initial orientation of the app’s user interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Details

- **Name**: `UIInterfaceOrientation` (Initial interface orientation)
- **Type**: string

## Possible Values

- `UIInterfaceOrientationPortrait`: The device is in portrait mode, with the device upright and the Home button on the bottom.
- `UIInterfaceOrientationPortraitUpsideDown`: The device is in portrait mode but is upside down, with the device upright and the Home button at the top.
- `UIInterfaceOrientationLandscapeLeft`: The device is in landscape mode, with the device upright and the Home button on the left.
- `UIInterfaceOrientationLandscapeRight`: The device is in landscape mode, with the device upright and the Home button on the right.



**Default**: `UIInterfaceOrientationPortrait`

#### Discussion

The default value is `UIInterfaceOrientationPortrait`. If you add the [`UISupportedInterfaceOrientations`](./uisupportedinterfaceorientations.md) key to the information property list, the system ignores this key.

For more information, see [`UIInterfaceOrientation`](../../UIKit/uiinterfaceorientation.md).

## See Also

### Orientation
- [UISupportedInterfaceOrientations](./uisupportedinterfaceorientations.md)
  The interface orientations supported by your app.
- [UIPreferredDefaultInterfaceOrientation](./uipreferreddefaultinterfaceorientation.md)
  A string that indicates the preferred initial interface orientation for iPad and iPhone apps running on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiinterfaceorientation)*