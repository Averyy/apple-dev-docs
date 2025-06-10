# init(source:)

**Framework**: SceneKit  
**Kind**: init

Initializes an audio player for playing the specified simple audio source.

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
init(source: SCNAudioSource)
```

#### Return Value

A positional audio player object.

#### Discussion

Using this initializer is typically not necessary. Instead, call the [`audioPlayerWithSource:`](scnaudioplayer/audioplayerwithsource:.md) method, which returns a cached audio player object if one for the specified audio source has already been created and is available for use.

## Parameters

- `source`: An audio source object.

## See Also

- [init(avAudioNode: AVAudioNode)](scnaudioplayer/init(avaudionode:).md)
  Initializes an audio player for playing the specified AVFoundation audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/init(source:))*