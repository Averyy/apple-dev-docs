# finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration:error:)

**Framework**: ReplayKit  
**Kind**: method

Applies configuration update changes to the next MP4 movie clip.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration broadcastConfiguration: RPBroadcastConfiguration?, error: (any Error)?)
```

#### Discussion

Call this method when processing is complete. After this method is called, whether an error exists or not, the current MP4 movie clip is no longer available.

## Parameters

- `broadcastConfiguration`: Optional configuration update that is applied to the next MP4 movie clip.
- `error`: Indicates that an error occurred with the broadcast, and broadcasting is to stop.

## See Also

- [func processMP4Clip(with: URL?, setupInfo: [String : NSObject]?, finished: Bool)](rpbroadcastmp4cliphandler/processmp4clip(with:setupinfo:finished:).md)
  Processes MP4 movie clips for a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/finishedprocessingmp4clip(withupdatedbroadcastconfiguration:error:))*