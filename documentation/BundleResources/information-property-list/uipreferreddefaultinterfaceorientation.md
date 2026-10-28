# UIPreferredDefaultInterfaceOrientation

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string that indicates the preferred initial interface orientation for iPad and iPhone apps running on visionOS.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Details

- **Name**: `UIPreferredDefaultInterfaceOrientation`
- **Type**: string

## Possible Values

- `UIInterfaceOrientationPortrait`
- `UIInterfaceOrientationPortraitUpsideDown`
- `UIInterfaceOrientationLandscapeLeft`
- `UIInterfaceOrientationLandscapeRight`

## Discussion

When compatible iPad and iPhone apps run on visionOS, the system references this key to determine the preferred initial interface orientation for the content that appears in a window in the person’s surroundings. This key is optional, and applications that don’t provide a value receive a default interface orientation that the system provides. The system evaluates the key, but might use a different value. For example, if a pre-existing state exists, that state defines the interface orientation. If a preferred interface orientation doesn’t exist in the app’s [`UISupportedInterfaceOrientations`](./uisupportedinterfaceorientations.md), the app receives a default interface orientation provided by the system – landscape right for iPad apps, portrait for iPhone apps.

> **Note**:  This key doesn’t apply to app’s built against the visionOS SDK.

## See Also

### Orientation
- [UIInterfaceOrientation](./uiinterfaceorientation.md)
  The initial orientation of the app’s user interface.
- [UISupportedInterfaceOrientations](./uisupportedinterfaceorientations.md)
  The interface orientations supported by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uipreferreddefaultinterfaceorientation)*