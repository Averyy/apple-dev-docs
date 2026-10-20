# init(source:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio player for playing the specified simple audio source.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init(source: SCNAudioSource)
```

```objc
- (instancetype) initWithSource:(SCNAudioSource *) source;
```

#### Return Value

A positional audio player object.

#### Discussion

Using this initializer is typically not necessary. Instead, call the [`audioPlayerWithSource:`](./audioplayerwithsource_.md) method, which returns a cached audio player object if one for the specified audio source has already been created and is available for use.

## Parameters

- `source`: An audio source object.

## See Also

### Creating an Audio Player
- [init(avAudioNode: AVAudioNode)](./init%28avaudionode%29-4u514.md)
  Initializes an audio player for playing the specified AVFoundation audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudioplayer/init(source:))*