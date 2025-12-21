# send(videoFrame:presentationTimeStamp:frameDuration:metadata:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends a video frame to all the connected receivers using its sample buffer representation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func send(videoFrame: ImmersiveVideoFrame, presentationTimeStamp: CMTime, frameDuration: CMTime, metadata: [PresentationCommand] = []) async throws
```

#### Discussion

> **Note**: This function throws if anything fails while sending the frame, for example, if the frame has an invalid format or data.

## Parameters

- `videoFrame`: The video frame to be sent to the receivers.
- `presentationTimeStamp`: The presentation time stamp of the frame.
- `frameDuration`: The duration of the frame in seconds.
- `metadata`: Metadata information to be send with this frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(videoframe:presentationtimestamp:frameduration:metadata:))*