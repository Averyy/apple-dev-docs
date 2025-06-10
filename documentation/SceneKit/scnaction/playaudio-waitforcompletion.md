# playAudio(_:waitForCompletion:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that plays an audio source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func playAudio(_ source: SCNAudioSource, waitForCompletion wait: Bool) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, SceneKit plays the audio source on the target node—any positional audio effects are based on the node’s position. For more information about positional audio in SceneKit, see [`SCNAudioPlayer`](scnaudioplayer.md).

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `source`: The audio source to play.
- `wait`: If  , the duration of this action is the same as the length of the audio playback. If  , the action is considered to have completed immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/playaudio(_:waitforcompletion:))*