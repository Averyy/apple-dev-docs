# processMP4Clip(with:setupInfo:finished:)

**Framework**: ReplayKit  
**Kind**: method

Processes MP4 movie clips for a live broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func processMP4Clip(with mp4ClipURL: URL?, setupInfo: [String : NSObject]?, finished: Bool)
```

## Parameters

- `mp4ClipURL`: URL that points to the location of the movie clip. This parameter is   when an error occurs.
- `setupInfo`: Dictionary that is supplied by the UI extension and contains setup information required for processing. The values contained in the dictionary are defined by the extension developer.
- `finished`: Boolean value indicating that the app has requested the broadcast to end. Set to   to end the broadcast.

## See Also

- [func finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: (any Error)?)](rpbroadcastmp4cliphandler/finishedprocessingmp4clip(withupdatedbroadcastconfiguration:error:).md)
  Applies configuration update changes to the next MP4 movie clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/processmp4clip(with:setupinfo:finished:))*