# AVPlayerViewControllerDelegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol AVPlayerViewControllerDelegate <NSObject>
```

## Mentions

- [Adopting Picture in Picture in a standard player](./adopting-picture-in-picture-in-a-standard-player.md)
- [Presenting content proposals in tvOS](./presenting-content-proposals-in-tvos.md)
- [Working with interstitial content](./working-with-interstitial-content.md)

## Topics

### Dismissing the player view controller
- [func playerViewControllerShouldDismiss(AVPlayerViewController) -> Bool](./avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss%28_%29.md)
  Asks the delegate object whether the player view controller dismisses itself upon request.
- [func playerViewControllerWillBeginDismissalTransition(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition%28_%29.md)
  Tells the delegate when the player view controller is about to start its dismissal transition.
- [func playerViewControllerDidEndDismissalTransition(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition%28_%29.md)
  Tells the delegate when the player view controller ends its dismissal transition.
### Responding to Picture in Picture life cycle events
- [func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(AVPlayerViewController) -> Bool](./avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart%28_%29.md)
  Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [func playerViewControllerWillStartPictureInPicture(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to start.
- [func playerViewControllerDidStartPictureInPicture(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerdidstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture starts.
- [func playerViewController(AVPlayerViewController, failedToStartPictureInPictureWithError: any Error)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,failedtostartpictureinpicturewitherror%29.md)
  Tells the delegate when Picture in Picture fails to start.
- [func playerViewControllerWillStopPictureInPicture(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerwillstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to stop.
- [func playerViewControllerDidStopPictureInPicture(AVPlayerViewController)](./avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture stops.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,restoreuserinterfaceforpictureinpicturestopwithcompletionhandler%29.md)
  Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.
### Responding to navigation events
- [func playerViewController(AVPlayerViewController, timeToSeekAfterUserNavigatedFrom: CMTime, to: CMTime) -> CMTime](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,timetoseekafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [func playerViewController(AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom: CMTime, to: CMTime)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willresumeplaybackafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user navigates to a new time and playback is about to begin.
- [func skipToPreviousItem(for: AVPlayerViewController)](./avplayerviewcontrollerdelegate/skiptopreviousitem%28for%29.md)
  Tells the delegate when the user requests skipping to the previous item in the timeline.
- [func skipToNextItem(for: AVPlayerViewController)](./avplayerviewcontrollerdelegate/skiptonextitem%28for%29.md)
  Tells the delegate when the user requests skipping to the next item in the timeline.
### Responding to interstitial content playback events
- [func playerViewController(AVPlayerViewController, willPresent: AVInterstitialTimeRange)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willpresent%29.md)
  Tells the delegate when the player view controller is about to start playing a range of interstitial content.
- [func playerViewController(AVPlayerViewController, didPresent: AVInterstitialTimeRange)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,didpresent%29.md)
  Tells the delegate when the player view controller finishes playing a range of interstitial content.
### Responding to content proposals
- [func playerViewController(AVPlayerViewController, shouldPresent: AVContentProposal) -> Bool](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,shouldpresent%29.md)
  Asks the delegate whether the player view controller presents a content proposal.
- [func playerViewController(AVPlayerViewController, didAccept: AVContentProposal)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,didaccept%29.md)
  Tells the delegate when the user accepts the proposed content.
- [func playerViewController(AVPlayerViewController, didReject: AVContentProposal)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,didreject%29.md)
  Tells the delegate when the user rejects the proposed content.
### Responding to media selection
- [func playerViewController(AVPlayerViewController, didSelect: AVMediaSelectionOption?, in: AVMediaSelectionGroup)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,didselect,in%29.md)
  Tells the delegate when the user selects a media option from a media selection group.
- [- playerViewController:didSelectExternalSubtitleOptionLanguage:](./avplayerviewcontrollerdelegate/playerviewcontroller_didselectexternalsubtitleoptionlanguage_.md)
  Tells the delegate when the user selects a specific subtitle option.
### Responding to transport bar changes
- [func playerViewController(AVPlayerViewController, willTransitionToVisibilityOfTransportBar: Bool, with: any AVPlayerViewControllerAnimationCoordinator)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willtransitiontovisibilityoftransportbar,with%29.md)
  Tells the delegate when the transport bar’s visibility is about to change.
- [protocol AVPlayerViewControllerAnimationCoordinator](./avplayerviewcontrolleranimationcoordinator.md)
  A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.
### Responding to channel changes
- [func playerViewController(AVPlayerViewController, skipToNextChannel: (Bool) -> Void)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,skiptonextchannel%29.md)
  Tells the delegate when the user wants to skip to the next channel.
- [func playerViewController(AVPlayerViewController, skipToPreviousChannel: (Bool) -> Void)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,skiptopreviouschannel%29.md)
  Tells the delegate when the user wants to skip to the previous channel.
- [func nextChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./avplayerviewcontrollerdelegate/nextchannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [func previousChannelInterstitialViewController(for: AVPlayerViewController) -> UIViewController](./avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller%28for%29.md)
  Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.
### Responding to full-screen presentations
- [func playerViewController(AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willbeginfullscreenpresentationwithanimationcoordinator%29.md)
  Tells the delegate when the player view controller is about to start full-screen display.
- [func playerViewController(AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,willendfullscreenpresentationwithanimationcoordinator%29.md)
  Tells the delegate when the player view controller is about to end full-screen display.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](./avplayerviewcontrollerdelegate/playerviewcontroller%28_,restoreuserinterfaceforfullscreenexitwithcompletionhandler%29.md)
  Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Standard player interfaces
- [Playing video content in a standard user interface](./playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [Customizing the tvOS playback experience](./customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Adopting the system player interface in visionOS](./adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [class AVPlayerViewController](./avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [class AVPlayerView](./avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewDelegate](./avplayerviewdelegate.md)
  A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.
- [struct VideoPlayer](./videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate)*