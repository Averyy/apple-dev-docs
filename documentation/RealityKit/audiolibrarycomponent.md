# AudioLibraryComponent

**Framework**: RealityKit  
**Kind**: struct

A container for audio resources that you can look up by user-defined names.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct AudioLibraryComponent
```

#### Overview

`AudioLibraryComponent` serves as a container for audio resources, so that you can store loaded audio resources and associate them with an entity for playback using user-defined names. You may use any [`AudioResource`](audioresource.md) type, such as [`AudioFileResource`](audiofileresource.md) or [`AudioFileGroupResource`](audiofilegroupresource.md).

> **Note**: In memory, you can also use [`AudioBufferResource`](audiobufferresource.md), but this type doesn’t support serializing to disk or sharing via network.

Below is an example of how you can set this component in code:

```swift
// Create a new entity.
let humanEntity = Entity()

// Set up two audio file resources, and combine them in one group resource.
let walkFileResource = try AudioFileResource.load(named: "HumanWalk")
let jumpFileResource = try AudioFileResource.load(named: "HumanJump")
let groupResource = try AudioFileGroupResource([walkFileResource, jumpFileResource])

// Create an `AudioLibraryComponent` to house the audio resources.
var audioLibraryComponent = AudioLibraryComponent()

// Add the resources to the component by name.
audioLibraryComponent.resources["Walk"] = walkFileResource
audioLibraryComponent.resources["Jump"] = jumpFileResource
audioLibraryComponent.resources["group"] = groupResource

humanEntity.components.set(audioLibraryComponent)

// Play the resource matching the "Walk" key on the entity -> Expect to play 'HumanWalk'.
humanEntity.playAudio(audioLibraryComponent.resources["Walk"]!)
```

By setting an `AudioLibraryComponent` on different entities, you can use simple defined names that trigger different sounds on different entities. For example, you can reuse the “Walk” string from the preceding example on a different entity:

```swift

// Create a new entity.
let robotEntity = Entity()

// Set up an audio file resource.
let robotWalkFileResource = try AudioFileResource.load(named: "RobotWalk")

// Create an `AudioLibraryComponent` to house the `audioResource`.
var audioLibraryComponent = AudioLibraryComponent()

// Add the resource to the component by name.
audioLibraryComponent.resources["Walk"] = robotWalkFileResource

robotEntity.components.set(audioLibraryComponent)

// Play the resource matching the "Walk" key on the entity -> Expect to play 'RobotWalk'.
robotEntity.playAudio(audioLibraryComponent.resources["Walk"]!)
```

> **Note**: You can create a component using code, or add it to your entity using tools such as Reality Composer Pro.

In Reality Composer Pro, you can add an `AudioLibraryComponent` to an entity and then add audio resources to it for easy access to those resources by name. The system automatically loads the audio resources for you when you search for this component.

```swift
guard let audioLibraryComponent = entity.components[AudioLibraryComponent.self],
      let audioResource = audioLibraryComponent.resources["My_Audio_Resource_Name"]
else { return }

// Because the system has already loaded the resource for you,
// you may prepare or play it on an entity right away.
entity.playAudio(audioResource)
```

## Topics

### Creating an audio library component
- [init(resources: [String : AudioResource])](audiolibrarycomponent/init(resources:).md)
  Creates a new audio library from a dictionary.
### Accessing audio resources
- [var resources: [String : AudioResource]](audiolibrarycomponent/resources.md)
  A dictionary of audio resources with user-defined names.

## Relationships

### Conforms To
- [Component](component.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)

## See Also

- [class AudioFileResource](audiofileresource.md)
  An audio resource that you load from a file or from a URL.
- [class AudioFileGroupResource](audiofilegroupresource.md)
  An audio file group.
- [class AudioBufferResource](audiobufferresource.md)
  An audio resource that you load from an [`AVAudioBuffer`](https://developer.apple.com/documentation/AVFAudio/AVAudioBuffer).
- [class AudioResource](audioresource.md)
  A playable audio resource


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiolibrarycomponent)*