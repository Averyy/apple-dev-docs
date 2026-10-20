# skipToPreviousItem(for:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user requests skipping to the previous item in the timeline.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func skipToPreviousItem(for playerViewController: AVPlayerViewController)
```

```objc
- (void) skipToPreviousItemForPlayerViewController:(AVPlayerViewController *) playerViewController;
```

#### Discussion

The framework calls this method when you set the player view controller’s skipping behavior to [`AVPlayerViewControllerSkippingBehavior.skipItem`](../avplayerviewcontrollerskippingbehavior/skipitem.md) and a user performs a backward skip gesture (by pressing the left side of the Siri Remote’s Touch surface). Implement this method to update the player view controller’s [`player`](../avplayerviewcontroller/player.md) to play the previous player item.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Responding to navigation events
- [func playerViewController(AVPlayerViewController, timeToSeekAfterUserNavigatedFrom: CMTime, to: CMTime) -> CMTime](./playerviewcontroller%28_,timetoseekafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [func playerViewController(AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom: CMTime, to: CMTime)](./playerviewcontroller%28_,willresumeplaybackafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user navigates to a new time and playback is about to begin.
- [func skipToNextItem(for: AVPlayerViewController)](./skiptonextitem%28for%29.md)
  Tells the delegate when the user requests skipping to the next item in the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/skiptopreviousitem(for:))*