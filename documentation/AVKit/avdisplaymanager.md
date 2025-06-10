# AVDisplayManager

**Framework**: AVKit  
**Kind**: class

A tvOS management object that controls whether a TV switches modes to match the video’s native mode.

**Availability**:
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
class AVDisplayManager
```

#### Overview

If you set the display manager’s [`preferredDisplayCriteria`](avdisplaymanager/preferreddisplaycriteria.md), when a user enables a Match Content setting, the TV attempts to change modes to match the currently playing video’s native display criteria.

> ❗ **Important**:  Don’t directly instantiate a display manager object. Instead, access the current instance from the key window’s [`avDisplayManager`](https://developer.apple.com/documentation/UIKit/UIWindow/avDisplayManager) property.

## Topics

### Matching a Video’s Native Display Mode
- [var preferredDisplayCriteria: AVDisplayCriteria?](avdisplaymanager/preferreddisplaycriteria.md)
  A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [var isDisplayCriteriaMatchingEnabled: Bool](avdisplaymanager/isdisplaycriteriamatchingenabled.md)
  A Boolean value that indicates whether the user has enabled display critera matching.
- [var isDisplayModeSwitchInProgress: Bool](avdisplaymanager/isdisplaymodeswitchinprogress.md)
  A Boolean value that indicates whether a display mode switch is in progress.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaymanager)*