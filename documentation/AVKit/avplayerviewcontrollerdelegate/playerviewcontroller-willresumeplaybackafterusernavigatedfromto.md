# playerViewController(_:willResumePlaybackAfterUserNavigatedFrom:to:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the user navigates to a new time and playback is about to begin.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom oldTime: CMTime, to targetTime: CMTime)
```

#### Discussion

Unlike the [`timeJumpedNotification`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/timeJumpedNotification) notification, this method fires only for complete, user-initiated navigation events. For example, if the user begins scrubbing through the media timeline and pauses several times before resuming playback, the player view controller calls this method only once.

You can use this method to present interstitial content before resuming playback, however, it’s recommended to use [`playerViewController(_:timeToSeekAfterUserNavigatedFrom:to:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:).md) for this purpose.

## Parameters

- `playerViewController`: The player view controller.
- `oldTime`: The current playback time before the user began navigating.
- `targetTime`: The new time where playback is about to resume.

## See Also

- [func playerViewController(AVPlayerViewController, timeToSeekAfterUserNavigatedFrom: CMTime, to: CMTime) -> CMTime](avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:).md)
  Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [func skipToPreviousItem(for: AVPlayerViewController)](avplayerviewcontrollerdelegate/skiptopreviousitem(for:).md)
  Tells the delegate when the user requests skipping to the previous item in the timeline.
- [func skipToNextItem(for: AVPlayerViewController)](avplayerviewcontrollerdelegate/skiptonextitem(for:).md)
  Tells the delegate when the user requests skipping to the next item in the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willresumeplaybackafterusernavigatedfrom:to:))*