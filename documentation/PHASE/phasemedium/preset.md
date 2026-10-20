# PHASEMedium.Preset

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Predetermined qualities of an environment that affect how sound transmits.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Preset
```

```c
enum PHASEMediumPreset : NSInteger;
```

#### Overview

Currently, this enumeration refers only to sound traveling through air.

## Topics

### Medium Types
- [PHASEMedium.Preset.air](./preset/air.md)
  A medium that simulates sound traveling through air.
### Initializers
- [init?(rawValue: Int)](./preset/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Medium
- [init(engine: PHASEEngine, preset: PHASEMedium.Preset)](./init%28engine,preset%29.md)
  Creates a medium.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemedium/preset)*