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

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access) entitlement to use the camera in PiP mode.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [var activeVideoCallSourceView: UIView?](avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview.md)
  The view that contains the video content of the call.
- [var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController](avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller.md)
  The view controller that presents the video call content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturevideocallviewcontroller)*