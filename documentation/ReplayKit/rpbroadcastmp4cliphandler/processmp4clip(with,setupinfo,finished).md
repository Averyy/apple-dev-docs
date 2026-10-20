# processMP4Clip(with:setupInfo:finished:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Processes MP4 movie clips for a live broadcast.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
func processMP4Clip(with mp4ClipURL: URL?, setupInfo: [String : NSObject]?, finished: Bool)
```

```objc
- (void) processMP4ClipWithURL:(NSURL *) mp4ClipURL setupInfo:(NSDictionary<NSString *,NSObject *> *) setupInfo finished:(BOOL) finished;
```

## Parameters

- `mp4ClipURL`: URL that points to the location of the movie clip. This parameter is `nil` when an error occurs.
- `setupInfo`: Dictionary that is supplied by the UI extension and contains setup information required for processing. The values contained in the dictionary are defined by the extension developer.
- `finished`: Boolean value indicating that the app has requested the broadcast to end. Set to [`true`](../../Swift/true.md) to end the broadcast.

## See Also

### Processing MP4 Movie Clips
- [func finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: (any Error)?)](./finishedprocessingmp4clip%28withupdatedbroadcastconfiguration,error%29.md)
  Applies configuration update changes to the next MP4 movie clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/processmp4clip(with:setupinfo:finished:))*