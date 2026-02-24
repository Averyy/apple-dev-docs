# addBoundaryTimeObserver(forTimes:queue:using:)

**Framework**: AVFoundation  
**Kind**: method

Requests the invocation of a block when specified times are traversed during normal playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
func addBoundaryTimeObserver(forTimes times: [NSValue], queue: dispatch_queue_t?, using block: @escaping @Sendable () -> Void) -> Any
```

## Mentions

- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md)

#### Return Value

An opaque object that you pass as the argument to [`removeTimeObserver(_:)`](avplayer/removetimeobserver(_:).md) to stop observation.

#### Discussion

Boundary times are arbitrary points of interest you define within the media timeline. As these times are traversed during normal playback, the block you provide to this method will be invoked. You must maintain a strong reference to the returned value as long as you want the time observer to be invoked by the player. Each invocation of this method should be paired with a corresponding call to [`removeTimeObserver(_:)`](avplayer/removetimeobserver(_:).md).

The player does not guarantee the callback block will always be invoked for each boundary time. If your times are very close together along the timeline (close enough that the execution of the block for one takes longer than the difference between them) or if a seek causes time to jump over one or more boundary times, time observation for any specific boundary time may not occur. The best practice is therefore to implement the callback block so it always performs its necessary calculations based solely on the player’s [`currentTime()`](avplayer/currenttime().md).

The following example shows how you could define boundary times for each quarter of playback.

**Swift**:

```swift
func addBoundaryTimeObserver() {
    var times = [NSValue]()
    // Set initial time to zero
    var currentTime = CMTime.zero
    // Divide the asset's duration into quarters.
    let interval = CMTimeMultiplyByFloat64(asset.duration, multiplier: 0.25)
    
    // Build boundary times at 25%, 50%, 75%, 100%
    while currentTime < asset.duration {
        currentTime = currentTime + interval
        times.append(NSValue(time: currentTime))
    }
    
    // Add time observer. Observe boundary time changes on the main queue.
    timeObserverToken = player.addBoundaryTimeObserver(forTimes: times,
                                                       queue: .main) { [weak self] in
        // Update UI
    }
}
```

**Objective-C**:

```objc
- (void)addBoundaryTimeObserver {
    NSMutableArray *times = [NSMutableArray array];
 
    // Set initial time to zero
    CMTime currentTime = kCMTimeZero;
    // Get asset duration
    CMTime assetDuration = self.asset.duration;
    // Divide the asset duration into quarters
    CMTime interval = CMTimeMultiplyByFloat64(assetDuration, 0.25);
 
    // Build boundary times at 25%, 50%, 75%, 100%
    while (CMTIME_COMPARE_INLINE(currentTime, <, assetDuration)) {
        currentTime = CMTimeAdd(currentTime, interval);
        [times addObject:[NSValue valueWithCMTime:currentTime]];
    }
    // Add time observer
    self.timeObserverToken =
        [self.player addBoundaryTimeObserverForTimes:times
                                               queue:dispatch_get_main_queue()
                                          usingBlock:^{
            // Use weak reference to self
            // Update user interface state
        }];
}
```

> ❗ **Important**:  Use a `weak` reference to `self` in the callback block to prevent creating a retain cycle.

## Parameters

- `times`: An array of `NSValue` objects containing [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) values that represent the times at which to invoke the callback. The system raises an exception if you pass an empty array.
- `queue`: A *serial* queue onto which `block` should be enqueued. Passing a concurrent queue is not supported and will result in undefined behavior. If you pass `nil`, the main queue is used.
- `block`: The block to be invoked when any of the times in `times` is crossed during normal playback.

## See Also

- [func currentTime() -> CMTime](avplayer/currenttime.md)
  Returns the current time of the current player item.
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avplayer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests the periodic invocation of a given block during playback to report changing time.
- [func removeTimeObserver(Any)](avplayer/removetimeobserver(_:).md)
  Cancels a previously registered periodic or boundary time observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/addboundarytimeobserver(fortimes:queue:using:))*