# setIsNowPlayingCandidate(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets a Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func setIsNowPlayingCandidate(_ inValue: Bool) throws
```

#### Discussion

Only a single audio session for an app can be a Now Playing candidate. Designating multiple audio sessions for the same app as Now Playing candidates results in none of them being eligible.

## Parameters

- `inValue`: The new state to set.

## See Also

- [var intendedSpatialExperience: any AVAudioSessionSpatialExperience](avaudiosession/intendedspatialexperience-1bpnq.md)
  The spatial audio experience your app intends to provide the user.
- [func setIntendedSpatialExperience(any AVAudioSessionSpatialExperience) throws](avaudiosession/setintendedspatialexperience(_:).md)
  Sets the spatial audio experience your app intends to provide the user.
- [protocol AVAudioSessionSpatialExperience](avaudiosessionspatialexperience-swift.protocol.md)
- [var isNowPlayingCandidate: Bool](avaudiosession/isnowplayingcandidate.md)
  A Boolean value that indicates whether the audio session is a candidate to be the Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setisnowplayingcandidate(_:))*