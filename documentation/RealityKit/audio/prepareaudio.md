# prepareAudio(_:)

**Framework**: RealityKit  
**Kind**: method

Prepares multiple audio resources for synchronized playback without starting them.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func prepareAudio(_ resourcesAndEntities: [(AudioResource, Entity)]) throws -> AudioPlaybackGroupController
```

#### Return Value

A controller that coordinates playback of the synchronized group.

#### Discussion

Use this method to set up a group of audio sources that you want to play together. Each resource is paired with the entity that emits it. Call [`play()`](audioplaybackgroupcontroller/play().md) or [`play(at:)`](audioplaybackgroupcontroller/play(at:).md) to begin playback.

> **Note**: An error if audio preparation fails.

## Parameters

- `resourcesAndEntities`: An array of tuples pairing each audio resource with the entity that emits it. The same entity may appear multiple times with different resources, and a single entity can participate in multiple groups.

## See Also

- [static func playAudio([(AudioResource, Entity)]) throws -> AudioPlaybackGroupController](audio/playaudio(_:).md)
  Prepares and plays multiple audio resources for synchronized playback
- [static func playAudio([(AudioResource, Entity)], at: AVAudioTime) throws -> AudioPlaybackGroupController](audio/playaudio(_:at:).md)
  Prepares and plays multiple audio resources for synchronized playback at a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/prepareaudio(_:))*