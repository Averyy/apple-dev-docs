# load()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Loads audio data from the source and prepares it for playing.

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
func load()
```

```objc
- (void) load;
```

#### Discussion

This method reads audio data from the source file (specified when initializing the audio source) and performs any decompression necessary to prepare for playing audio. Use this method to control when your app or game incurs the run-time performance cost of such work—for example, you can load all audio source before starting a game level, instead of suffering a frame rate drop upon playing a new audio source during gameplay.

This method has no effect if the [`shouldStream`](./shouldstream.md) property’s value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaudiosource/load())*