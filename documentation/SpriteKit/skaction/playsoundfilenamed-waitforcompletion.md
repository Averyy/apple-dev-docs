# playSoundFileNamed(_:waitForCompletion:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that plays a sound.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

Use [`SKAction`](skaction.md) `playSoundFileNamed:waitForCompletion:` only for short incidentals. Use [`AVAudioPlayer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer) for long running background music. This action is not reversible; the reversed action is identical to the original action.

## Parameters

- `soundFile`: The name of a sound file in the app’s bundle.
- `wait`: If  , the duration of this action is the same as the length of the audio playback. If  , the action is considered to have completed immediately.

## See Also

- [class func play() -> SKAction](skaction/play.md)
  Creates an action that tells an audio node to start playback.
- [class func pause() -> SKAction](skaction/pause.md)
  Creates an action that tells an audio node to pause playback.
- [class func stop() -> SKAction](skaction/stop.md)
  Creates an action that tells an audio node to stop playback.
- [class func changePlaybackRate(to: Float, duration: TimeInterval) -> SKAction](skaction/changeplaybackrate(to:duration:).md)
  Creates an action that changes an audio node’s playback rate to a new value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/playsoundfilenamed(_:waitforcompletion:))*