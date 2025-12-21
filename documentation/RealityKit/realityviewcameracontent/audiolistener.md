# audioListener

**Framework**: RealityKit  
**Kind**: property

The entity which defines the listener position and orientation for spatial audio.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
var audioListener: Entity? { get set }
```

#### Discussion

By default this `audioListener` property is nil, which means that the active camera entity will be used as the audio listener. The `audioListener` can be set to any entity in the `scene` to use the transform of the entity as the audio listener position and orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/audiolistener)*