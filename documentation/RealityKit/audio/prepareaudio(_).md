# prepareAudio(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Prepares multiple audio resources for synchronized playback without starting them.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
static func prepareAudio(_ resourcesAndEntities: [(AudioResource, Entity)]) throws -> AudioPlaybackGroupController
```

## Return Value

A controller that coordinates playback of the synchronized group.

## Discussion

Use this method to set up a group of audio sources that you want to play together. Each resource is paired with the entity that emits it. Call [`play()`](../audioplaybackgroupcontroller/play%28%29.md) or [`play(at:)`](../audioplaybackgroupcontroller/play%28at%29.md) to begin playback.

> **Throws**: An error if audio preparation fails.

## Parameters

- `resourcesAndEntities`: An array of tuples pairing each audio resource with the entity that emits it. The same entity may appear multiple times with different resources, and a single entity can participate in multiple groups.

## See Also

### Playing audio resources
- [static func playAudio([(AudioResource, Entity)]) throws -> AudioPlaybackGroupController](./playaudio%28_%29.md)
  Prepares and plays multiple audio resources for synchronized playback
- [static func playAudio([(AudioResource, Entity)], at: AVAudioTime) throws -> AudioPlaybackGroupController](./playaudio%28_,at%29.md)
  Prepares and plays multiple audio resources for synchronized playback at a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/prepareaudio(_:))*