# init(named:inDirectory:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Loads a particle system from a file in the app’s bundle resources.

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
convenience init?(named name: String, inDirectory directory: String?)
```

```objc
+ (instancetype) particleSystemNamed:(NSString *) name inDirectory:(NSString *) directory;
```

#### Return Value

A new particle system instantiated from the contents of the file.

#### Discussion

A SceneKit particle file created by Xcode contains an archived [`SCNParticleSystem`](../scnparticlesystem.md) instance, so you can also use the [`NSKeyedArchiver`](../../Foundation/nskeyedarchiver.md) and [`NSKeyedUnarchiver`](../../Foundation/nskeyedunarchiver.md) classes to write and read particle files.

## Parameters

- `name`: The name of a particle system file in the app’s bundle resources directory, with or without the `.scnp` extension.
- `directory`: The subdirectory path in the app’s bundle resources directory.

## See Also

### Creating a Particle System
- [+ particleSystem](./particlesystem.md)
  Creates a new particle system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/init(named:indirectory:))*