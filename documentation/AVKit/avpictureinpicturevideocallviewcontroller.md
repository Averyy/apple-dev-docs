# AVPictureInPictureVideoCallViewController

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVPictureInPictureVideoCallViewController : UIViewController
```

## Mentions

- [Adopting Picture in Picture for video calls](./adopting-picture-in-picture-for-video-calls.md)

## Overview

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](../AVFoundation/avcapturesession/ismultitaskingcameraaccessenabled.md) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](../BundleResources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement to use the camera in PiP mode.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Picture in Picture
- [Adopting Picture in Picture in a standard player](./adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a custom player](./adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](./adopting-picture-in-picture-for-video-calls.md)
  Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Adopting Picture in Picture playback in tvOS](./adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [class AVPictureInPictureController](./avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.
- [protocol AVPictureInPictureControllerDelegate](./avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](./avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
- [protocol AVPlayerViewPictureInPictureDelegate](./avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturevideocallviewcontroller)*