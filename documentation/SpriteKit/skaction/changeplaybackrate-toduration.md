# changePlaybackRate(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes an audio node’s playback rate to a new value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func changePlaybackRate(to v: Float, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the audio node’s playback rate animates from its current value to its new value. For more information, see [`AVAudio3DMixing`](https://developer.apple.com/documentation/AVFAudio/AVAudio3DMixing).

This action is not reversible.

## Parameters

- `v`: The new value for the playback rate. A playback rate of   represents normal speed.
- `duration`: The duration of the animation, in seconds.

## See Also

- [class func playSoundFileNamed(String, waitForCompletion: Bool) -> SKAction](skaction/playsoundfilenamed(_:waitforcompletion:).md)
  Creates an action that plays a sound.
- [class func play() -> SKAction](skaction/play.md)
  Creates an action that tells an audio node to start playback.
- [class func pause() -> SKAction](skaction/pause.md)
  Creates an action that tells an audio node to pause playback.
- [class func stop() -> SKAction](skaction/stop.md)
  Creates an action that tells an audio node to stop playback.
- [class func changePlaybackRate(by: Float, duration: TimeInterval) -> SKAction](skaction/changeplaybackrate(by:duration:).md)
  Creates an action that changes an audio node’s playback rate by a relative amount.
- [class func changeVolume(to: Float, duration: TimeInterval) -> SKAction](skaction/changevolume(to:duration:).md)
  Creates an action that changes an audio node’s volume to a new value.
- [class func changeVolume(by: Float, duration: TimeInterval) -> SKAction](skaction/changevolume(by:duration:).md)
  Creates an action that changes an audio node’s volume by a relative value.
- [class func changeObstruction(to: Float, duration: TimeInterval) -> SKAction](skaction/changeobstruction(to:duration:).md)
  Creates an action that changes an audio node’s obstruction to a new value.
- [class func changeObstruction(by: Float, duration: TimeInterval) -> SKAction](skaction/changeobstruction(by:duration:).md)
  Creates an action that changes an audio node’s obstruction by a relative value.
- [class func changeOcclusion(to: Float, duration: TimeInterval) -> SKAction](skaction/changeocclusion(to:duration:).md)
  Creates an action that changes an audio node’s occlusion to a new value.
- [class func changeOcclusion(by: Float, duration: TimeInterval) -> SKAction](skaction/changeocclusion(by:duration:).md)
  Creates an action that changes an audio node’s occlusion by a relative value.
- [class func changeReverb(to: Float, duration: TimeInterval) -> SKAction](skaction/changereverb(to:duration:).md)
  Creates an action that changes an audio node’s reverb to a new value.
- [class func changeReverb(by: Float, duration: TimeInterval) -> SKAction](skaction/changereverb(by:duration:).md)
  Creates an action that changes an audio node’s reverb by a relative value.
- [class func stereoPan(to: Float, duration: TimeInterval) -> SKAction](skaction/stereopan(to:duration:).md)
  Creates an action that changes an audio node’s stereo panning to a new value.
- [class func stereoPan(by: Float, duration: TimeInterval) -> SKAction](skaction/stereopan(by:duration:).md)
  Creates an action that changes an audio node’s stereo panning by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/changeplaybackrate(to:duration:))*