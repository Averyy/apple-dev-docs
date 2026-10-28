# playerViewController(_:timeToSeekAfterUserNavigatedFrom:to:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, timeToSeekAfterUserNavigatedFrom oldTime: CMTime, to targetTime: CMTime) -> CMTime
```

```objc
- (CMTime) playerViewController:(AVPlayerViewController *) playerViewController timeToSeekAfterUserNavigatedFromTime:(CMTime) oldTime toTime:(CMTime) targetTime;
```

## Mentions

- [Working with interstitial content](../working-with-interstitial-content.md)

## Return Value

The time at which to begin playback.

## Discussion

The framework calls this method prior to beginning playback after a user-initiated scrubbing request. You can return a time value other than the specified target time if needed to enforce certain business rules. For instance, you may want to return a different time to prevent users from skipping past ad breaks in your program.

## Parameters

- `playerViewController`: The player view controller.
- `oldTime`: The current playback time before the user began navigating.
- `targetTime`: The time to which the user navigated.

## See Also

### Responding to navigation events
- [func playerViewController(AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom: CMTime, to: CMTime)](./playerviewcontroller%28_,willresumeplaybackafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user navigates to a new time and playback is about to begin.
- [func skipToPreviousItem(for: AVPlayerViewController)](./skiptopreviousitem%28for%29.md)
  Tells the delegate when the user requests skipping to the previous item in the timeline.
- [func skipToNextItem(for: AVPlayerViewController)](./skiptonextitem%28for%29.md)
  Tells the delegate when the user requests skipping to the next item in the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:timetoseekafterusernavigatedfrom:to:))*