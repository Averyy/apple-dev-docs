# loadSamplePresentationTime(forTrackTime:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads a sample presentation time that maps to the specified track time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadSamplePresentationTime(forTrackTime trackTime: CMTime, completionHandler: @escaping @Sendable (CMTime, (any Error)?) -> Void)
```

```swift
func loadSamplePresentationTime(forTrackTime trackTime: CMTime) async throws -> CMTime
```

```objc
- (void) loadSamplePresentationTimeForTrackTime:(CMTime) trackTime completionHandler:(void (^)(CMTime , NSError *)) completionHandler;
```

## Parameters

- `trackTime`: The track time of the presentation time to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

  - **time**: A [`CMTime`](../../CoreMedia/cmtime.md) value, which is [`invalid`](../../CoreMedia/cmtime/invalid.md) if the track time is out of range or if an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading track segments
- [static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]>](../avpartialasyncproperty/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func loadSegment(forTrackTime: CMTime, completionHandler: (AVAssetTrackSegment?, (any Error)?) -> Void)](./loadsegment%28fortracktime,completionhandler%29.md)
  Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [class AVAssetTrackSegment](../avassettracksegment.md)
  An object that represents a time range segment of an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:))*