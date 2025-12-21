# send(taggedBuffers:presentationTimeStamp:frameDuration:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends a video frame to all the connected receivers using its tagged buffers representation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func send(taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, frameDuration: CMTime) async throws
```

#### Discussion

> **Note**: This function throws if anything fails while sending the frame, for example, if the frame has an invalid format or data.

## Parameters

- `presentationTimeStamp`: The presentation time stamp of the frame.
- `frameDuration`: The duration of the frame in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(taggedbuffers:presentationtimestamp:frameduration:))*