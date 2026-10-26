# audioPlayerWithSource:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Returns an audio player (creating one if necessary) to play a simple audio source.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) audioPlayerWithSource:(SCNAudioSource *) source;
```

#### Return Value

A positional audio player object.

#### Discussion

An [`SCNAudioSource`](../scnaudiosource.md) object represents a distinct source of audio (for example, a sound file) that can be reused and shared by many player objects. Use this method to create an audio player from such a source. When you use this method, SceneKit creates an audio player for the specified [`SCNAudioSource`](../scnaudiosource.md) object or, if an audio player for that source already exists and is not in use, SceneKit reuses the existing player object.

If instead you want to attach a more complex audio setup to a position in your scene—such as a mixer that varies several audio inputs in response to user input—build that setup using [`AVAudioNode`](../../AVFAudio/avaudionode.md) objects and create a player for it with the [`audioPlayerWithAVAudioNode:`](./audioplayerwithavaudionode_.md) method.

## Parameters

- `source`: An audio source object.

## See Also

### Creating an Audio Player
- [init(source: SCNAudioSource)](./init%28source%29.md)
  Initializes an audio player for playing the specified simple audio source.
- [init(avAudioNode: AVAudioNode)](./init%28avaudionode%29-4u514.md)
  Initializes an audio player for playing the specified AVFoundation audio node.
- [+ audioPlayerWithAVAudioNode:](./audioplayerwithavaudionode_.md)
  Returns an audio player (creating one if necessary) to play an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/audioplayerwithsource:)*