# skipToNextItem(for:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user requests skipping to the next item in the timeline.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
optional func skipToNextItem(for playerViewController: AVPlayerViewController)
```

```objc
- (void) skipToNextItemForPlayerViewController:(AVPlayerViewController *) playerViewController;
```

#### Discussion

The framework calls this method when you set the player view controller’s skipping behavior to [`AVPlayerViewControllerSkippingBehavior.skipItem`](../avplayerviewcontrollerskippingbehavior/skipitem.md) and a user performs a forward skip gesture (by pressing the right side of the Siri Remote’s Touch surface). Implement this method to update the player view controller’s [`player`](../avplayerviewcontroller/player.md) to play the next player item.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Responding to navigation events
- [func playerViewController(AVPlayerViewController, timeToSeekAfterUserNavigatedFrom: CMTime, to: CMTime) -> CMTime](./playerviewcontroller%28_,timetoseekafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [func playerViewController(AVPlayerViewController, willResumePlaybackAfterUserNavigatedFrom: CMTime, to: CMTime)](./playerviewcontroller%28_,willresumeplaybackafterusernavigatedfrom,to%29.md)
  Tells the delegate when the user navigates to a new time and playback is about to begin.
- [func skipToPreviousItem(for: AVPlayerViewController)](./skiptopreviousitem%28for%29.md)
  Tells the delegate when the user requests skipping to the previous item in the timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/skiptonextitem(for:))*