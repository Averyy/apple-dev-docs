# AVNavigationMarkersGroup

**Framework**: AVKit  
**Kind**: class

A set of markers for navigating playback of an audiovisual presentation.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class AVNavigationMarkersGroup
```

## Mentions

- [Presenting Navigation Markers](presenting-navigation-markers.md)

#### Overview

The most common form of a navigation markers group is a chapter list; however, you can also provide other sets of markers to allow a user to jump to significant events in the presentation. For example, a “Goals Scored” markers group might summarize key moments in a recorded sporting event. When you associate navigation markers with an [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) object you present with an [`AVPlayerViewController`](avplayerviewcontroller.md), the user interface provides options for navigating each group.

## Topics

### Creating a Navigation Marker Group
- [init(title: String?, timedNavigationMarkers: [AVTimedMetadataGroup])](avnavigationmarkersgroup/init(title:timednavigationmarkers:).md)
  Initializes a navigation markers group with the specified title and array of timed navigation markers.
- [init(title: String?, dateRangeNavigationMarkers: [AVDateRangeMetadataGroup])](avnavigationmarkersgroup/init(title:daterangenavigationmarkers:).md)
  Initializes a navigation markers group with the specified title and array of date range navigation markers.
### Inspecting Navigation Metadata
- [var title: String?](avnavigationmarkersgroup/title.md)
  The title of the marker group.
- [var timedNavigationMarkers: [AVTimedMetadataGroup]?](avnavigationmarkersgroup/timednavigationmarkers.md)
  The array of timed navigation markers for which the group provides navigation.
- [var dateRangeNavigationMarkers: [AVDateRangeMetadataGroup]?](avnavigationmarkersgroup/daterangenavigationmarkers.md)
  The array of date range navigation markers for which the group provides navigation.

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
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup)*