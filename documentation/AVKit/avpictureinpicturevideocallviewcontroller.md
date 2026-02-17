# AVPictureInPictureVideoCallViewController

**Framework**: AVKit  
**Kind**: class

A view controller that presents content from a video call in Picture in Picture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVPictureInPictureVideoCallViewController
```

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Overview

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/isMultitaskingCameraAccessEnabled) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.avfoundation.multitasking-camera-access) entitlement to use the camera in PiP mode.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [var activeVideoCallSourceView: UIView?](avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview.md)
  The view that contains the video content of the call.
- [var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController](avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller.md)
  The view controller that presents the video call content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturevideocallviewcontroller)*