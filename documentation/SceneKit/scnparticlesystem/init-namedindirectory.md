# init(named:inDirectory:)

**Framework**: SceneKit  
**Kind**: init

Loads a particle system from a file in the app’s bundle resources.

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
convenience init?(named name: String, inDirectory directory: String?)
```

#### Return Value

A new particle system instantiated from the contents of the file.

#### Discussion

A SceneKit particle file created by Xcode contains an archived [`SCNParticleSystem`](scnparticlesystem.md) instance, so you can also use the [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) and [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) classes to write and read particle files.

## Parameters

- `name`: The name of a particle system file in the app’s bundle resources directory, with or without the   extension.
- `directory`: The subdirectory path in the app’s bundle resources directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/init(named:indirectory:))*