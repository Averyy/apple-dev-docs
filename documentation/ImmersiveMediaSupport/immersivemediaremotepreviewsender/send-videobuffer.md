# send(videoBuffer:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends the video frame to the receivers.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func send(videoBuffer: CMSampleBuffer) async throws
```

#### Discussion

> **Note**: This function throws if anything fails while sending the frame, for example, if the frame has an invalid format or data.

## Parameters

- `videoBuffer`: The video buffer to be sent to the receivers - this needs to be a sample buffer with   equals to   and   containing frames properly tagged to be used as Immersive Video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(videobuffer:))*