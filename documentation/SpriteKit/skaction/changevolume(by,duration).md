# changeVolume(by:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes an audio node’s volume by a relative value.

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
class func changeVolume(by v: Float, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) changeVolumeBy:(float) v duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the audio node’s volume animates from its current value to its new value. For more information, see [`AVAudio3DMixing`](../../AVFAudio/avaudio3dmixing.md).

This action is reversible; the reverse is created as if the following code is executed:

**Swift**:

```swift
let action = SKAction.changeVolume(by: -v, duration: sec)
```

**Obj-C**:

```objc
[SKAction changeVolumeBy: -v duration: sec];
```

## Parameters

- `v`: The amount to change the volume by.
- `duration`: The duration of the animation, in seconds.

## See Also

### Controlling the Audio of a Node
- [class func playSoundFileNamed(String, waitForCompletion: Bool) -> SKAction](./playsoundfilenamed%28_,waitforcompletion%29.md)
  Creates an action that plays a sound.
- [class func play() -> SKAction](./play%28%29.md)
  Creates an action that tells an audio node to start playback.
- [class func pause() -> SKAction](./pause%28%29.md)
  Creates an action that tells an audio node to pause playback.
- [class func stop() -> SKAction](./stop%28%29.md)
  Creates an action that tells an audio node to stop playback.
- [class func changePlaybackRate(to: Float, duration: TimeInterval) -> SKAction](./changeplaybackrate%28to,duration%29.md)
  Creates an action that changes an audio node’s playback rate to a new value.
- [class func changePlaybackRate(by: Float, duration: TimeInterval) -> SKAction](./changeplaybackrate%28by,duration%29.md)
  Creates an action that changes an audio node’s playback rate by a relative amount.
- [class func changeVolume(to: Float, duration: TimeInterval) -> SKAction](./changevolume%28to,duration%29.md)
  Creates an action that changes an audio node’s volume to a new value.
- [class func changeObstruction(to: Float, duration: TimeInterval) -> SKAction](./changeobstruction%28to,duration%29.md)
  Creates an action that changes an audio node’s obstruction to a new value.
- [class func changeObstruction(by: Float, duration: TimeInterval) -> SKAction](./changeobstruction%28by,duration%29.md)
  Creates an action that changes an audio node’s obstruction by a relative value.
- [class func changeOcclusion(to: Float, duration: TimeInterval) -> SKAction](./changeocclusion%28to,duration%29.md)
  Creates an action that changes an audio node’s occlusion to a new value.
- [class func changeOcclusion(by: Float, duration: TimeInterval) -> SKAction](./changeocclusion%28by,duration%29.md)
  Creates an action that changes an audio node’s occlusion by a relative value.
- [class func changeReverb(to: Float, duration: TimeInterval) -> SKAction](./changereverb%28to,duration%29.md)
  Creates an action that changes an audio node’s reverb to a new value.
- [class func changeReverb(by: Float, duration: TimeInterval) -> SKAction](./changereverb%28by,duration%29.md)
  Creates an action that changes an audio node’s reverb by a relative value.
- [class func stereoPan(to: Float, duration: TimeInterval) -> SKAction](./stereopan%28to,duration%29.md)
  Creates an action that changes an audio node’s stereo panning to a new value.
- [class func stereoPan(by: Float, duration: TimeInterval) -> SKAction](./stereopan%28by,duration%29.md)
  Creates an action that changes an audio node’s stereo panning by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/changevolume(by:duration:))*