# playAudio(_:)

**Framework**: RealityKit  
**Kind**: method

Prepares and plays multiple audio resources for synchronized playback

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
@MainActor static func playAudio(_ resourcesAndEntities: [(AudioResource, Entity)]) throws -> AudioPlaybackGroupController
```

#### Return Value

An `AudioPlaybackGroupController` for the synchronized group.

#### Discussion

This method creates an `AudioPlaybackGroupController` that coordinates playback across multiple entity/resource pairs. All audio sources in the group will be synchronized to sample-accurate precision. After the controller is created, the [`play()`](audioplaybackgroupcontroller/play().md) method of the controller that it returns is immediately called.

> **Note**: An error if the audio preparation fails.

#### Usage Notes

- The same entity can be used with multiple resources in the same group
- Entities can participate in multiple groups simultaneously
- The completion handler fires when the longest resource finishes

## Parameters

- `resourcesAndEntities`: An array of tuples containing audio resources and their associated entities. The same entity can appear multiple times with different resources.

## See Also

- [static func playAudio([(AudioResource, Entity)], at: AVAudioTime) throws -> AudioPlaybackGroupController](audio/playaudio(_:at:).md)
  Prepares and plays multiple audio resources for synchronized playback at a specified time.
- [static func prepareAudio([(AudioResource, Entity)]) throws -> AudioPlaybackGroupController](audio/prepareaudio(_:).md)
  Prepares multiple audio resources for synchronized playback without starting them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/playaudio(_:))*