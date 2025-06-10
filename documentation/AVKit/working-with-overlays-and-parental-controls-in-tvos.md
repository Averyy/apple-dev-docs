# Working with Overlays and Parental Controls in tvOS

**Framework**: AVKit

Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.

**Availability**:
- tvOS 13.0+
- Xcode 15.3+

#### Overview

> **Note**: This sample code project is associated with WWDC 2019 session [`503: Delivering Intuitive Media Playback with AVKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc19/503/).

##### Configure the Sample Code Project

Only navigation from live streaming supports channel flipping, so you need to replace the assets in this sample with your live content to demonstrate this behavior.

By default, the sample demonstrates automatic support for parental controls. Activate parental restrictions by following the steps below:

1. Go to Settings > General > Restrictions.
2. Turn on Restrictions.
3. Set a passcode (1111 for demonstration purposes; remember this passcode).
4. Scroll down to the Allowed Content section.
5. Select Movies and/or TV Shows.
6. Set a restriction level (for example, PG or PG-13 if you are in the United States).

The first demo video has a rating of PG, and the second has a rating of PG-13. You can find or edit these ratings in `MainViewController.swift`.

This sample also demonstrates explicit support for parental restrictions by directly calling `playerItem.requestPlaybackRestrictionsAuthorization(_ completion)`. You can test explicit support by changing the value of `checkParentalControlsExplicitly` in the sample.

## See Also

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
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
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/working-with-overlays-and-parental-controls-in-tvos)*