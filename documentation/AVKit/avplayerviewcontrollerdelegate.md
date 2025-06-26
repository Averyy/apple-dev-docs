# AVPlayerViewControllerDelegate

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to implement to respond to player view controller events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVPlayerViewControllerDelegate : NSObjectProtocol
```

## Mentions

- [Adopting Picture in Picture in a Standard Player](adopting-picture-in-picture-in-a-standard-player.md)
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
- [Working with Interstitial Content](working-with-interstitial-content.md)

## Topics

### Dismissing the Player View Controller
- [func playerViewControllerShouldDismiss(AVPlayerViewController) -> Bool](avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(_:).md)
  Asks the delegate object whether the player view controller dismisses itself upon request.
- [func playerViewControllerWillBeginDismissalTransition(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition(_:).md)
  Tells the delegate when the player view controller is about to start its dismissal transition.
- [func playerViewControllerDidEndDismissalTransition(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(_:).md)
  Tells the delegate when the player view controller ends its dismissal transition.
### Responding to Picture in Picture Life Cycle Events
- [func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(AVPlayerViewController) -> Bool](avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(_:).md)
  Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [func playerViewControllerWillStartPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(_:).md)
  Tells the delegate when Picture in Picture is about to start.
- [func playerViewControllerDidStartPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate when Picture in Picture starts.
- [func playerViewController(AVPlayerViewController, failedToStartPictureInPictureWithError: any Error)](avplayerviewcontrollerdelegate/playerviewcontroller(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate when Picture in Picture fails to start.
- [func playerViewControllerWillStopPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerwillstoppictureinpicture(_:).md)
  Tells the delegate when Picture in Picture is about to stop.
- [func playerViewControllerDidStopPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate when Picture in Picture stops.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.
### Responding to Navigation Events
- [func playerViewController(AVPlayerViewController, timeToSeekAfterUserNavigatedFrom: CMTime, to: CMTime) -> CMTime](avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:).md)
  Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [func playerViewController(AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom: CMTime, to: CMTime)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willresumeplaybackafterusernavigatedfrom:to:).md)
  Tells the delegate when the user navigates to a new time and playback is about to begin.
- [func skipToPreviousItem(for: AVPlayerViewController)](avplayerviewcontrollerdelegate/skiptopreviousitem(for:).md)
  Tells the delegate when the user requests skipping to the previous item in the timeline.
- [func skipToNextItem(for: AVPlayerViewController)](avplayerviewcontrollerdelegate/skiptonextitem(for:).md)
  Tells the delegate when the user requests skipping to the next item in the timeline.
### Responding to Interstitial Content Playback Events
- [func playerViewController(AVPlayerViewController, willPresent: AVInterstitialTimeRange)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willpresent:).md)
  Tells the delegate when the player view controller is about to start playing a range of interstitial content.
- [func playerViewController(AVPlayerViewController, didPresent: AVInterstitialTimeRange)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didpresent:).md)
  Tells the delegate when the player view controller finishes playing a range of interstitial content.
### Responding to Content Proposals
- [func playerViewController(AVPlayerViewController, shouldPresent: AVContentProposal) -> Bool](avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:).md)
  Asks the delegate whether the player view controller presents a content proposal.
- [func playerViewController(AVPlayerViewController, didAccept: AVContentProposal)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:).md)
  Tells the delegate when the user accepts the proposed content.
- [func playerViewController(AVPlayerViewController, didReject: AVContentProposal)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:).md)
  Tells the delegate when the user rejects the proposed content.
### Responding to Media Selection
- [func playerViewController(AVPlayerViewController, didSelect: AVMediaSelectionOption?, in: AVMediaSelectionGroup)](avplayerviewcontrollerdelegate/playerviewcontroller(_:didselect:in:).md)
  Tells the delegate when the user selects a media option from a media selection group.
### Responding to Transport Bar Changes
- [func playerViewController(AVPlayerViewController, willTransitionToVisibilityOfTransportBar: Bool, with: any AVPlayerViewControllerAnimationCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willtransitiontovisibilityoftransportbar:with:).md)
  Tells the delegate when the transport bar’s visibility is about to change.
- [protocol AVPlayerViewControllerAnimationCoordinator](avplayerviewcontrolleranimationcoordinator.md)
  A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.
### Responding to Channel Changes
- [func playerViewController(AVPlayerViewController, skipToNextChannel: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptonextchannel:).md)
  Tells the delegate when the user wants to skip to the next channel.
- [func playerViewController(AVPlayerViewController, skipToPreviousChannel: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:skiptopreviouschannel:).md)
  Tells the delegate when the user wants to skip to the previous channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](avplayerviewcontrollerdelegate/nextchannelinterstitialviewcontroller(for:).md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [func previousChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for:).md)
  Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.
### Responding to Full-Screen Presentations
- [func playerViewController(AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:).md)
  Tells the delegate when the player view controller is about to start full-screen display.
- [func playerViewController(AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willendfullscreenpresentationwithanimationcoordinator:).md)
  Tells the delegate when the player view controller is about to end full-screen display.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:).md)
  Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [class AVCaptureEventInteraction](avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEvent](avcaptureevent.md)
  An object that describes a user interaction with a system hardware button.
- [class AVCaptureEventSound](avcaptureeventsound.md)
  A sound object for a capture event.
- [class AVInputPickerInteraction](avinputpickerinteraction.md)
  Use `AVInputPickerInteraction` to present an input picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate)*