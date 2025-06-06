# AVContinuityDevicePickerViewController

**Framework**: Avkit  
**Kind**: class

A view controller that provides an interface to a person so they can select and connect a continuity device to the system.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
@MainActor
class AVContinuityDevicePickerViewController
```

#### Overview

The view controller presents an interface on an Apple TV that lets a person choose a nearby continuity device ([`AVContinuityDevice`](https://developer.apple.com/documentation/AVFoundation/AVContinuityDevice)). Your app can then connect to that device’s cameras and microphones (see [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice) and [`AVAudioSessionPortDescription`](https://developer.apple.com/documentation/AVFAudio/AVAudioSessionPortDescription), respectively).

> ❗ **Important**:  The continuity device picker presents any devices near the Apple TV that use the same Apple ID.

To respond to the various outcome events from the picker, your app needs to implement the [`AVContinuityDevicePickerViewControllerDelegate`](avcontinuitydevicepickerviewcontrollerdelegate.md) and assign it to the picker’s [`delegate`](avcontinuitydevicepickerviewcontroller/delegate.md) property.

> **Note**:  SwiftUI apps can present the same interface with the `VideoPlayer/continuityDevicePicker(isPresented:onDidConnect:)` view modifier.

## Topics

### Checking for feature support
- [class var isSupported: Bool](avcontinuitydevicepickerviewcontroller/issupported.md)
  A Boolean value that indicates whether the system supports connecting to a continuity device.
### Designating a delegate
- [var delegate: (any AVContinuityDevicePickerViewControllerDelegate)?](avcontinuitydevicepickerviewcontroller/delegate.md)
  The delegate that responds to events from the continuity device picker view controller.

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
- [Sendable](../Swift/Sendable.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVKit/avcontinuitydevicepickerviewcontroller)*