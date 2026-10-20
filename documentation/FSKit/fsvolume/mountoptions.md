# FSVolume.MountOptions

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Mount options to be requested from FSKit using the `requestedMountOptions` property.

**Availability**:
- macOS 26.4+

## Declaration

```swift
struct MountOptions
```

```c
enum FSMountOptions : NSUInteger;
```

## Topics

### Inspecting mount options
- [static var readOnly: FSVolume.MountOptions](./mountoptions/readonly.md)
  An option to request a read-only mount.
### Working with raw values
- [init(rawValue: UInt)](./mountoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/mountoptions)*