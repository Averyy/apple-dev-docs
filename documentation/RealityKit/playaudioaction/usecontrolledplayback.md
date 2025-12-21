# useControlledPlayback

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether this action has control over the playback of the audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var useControlledPlayback: Bool
```

#### Discussion

Setting the value of this property to true indicates the action has control over the playback of the audio. Setting this to false indicates the audio plays independently from the action, behaving like a one shot audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playaudioaction/usecontrolledplayback)*