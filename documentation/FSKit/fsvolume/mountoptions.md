# FSVolume.MountOptions

**Framework**: FSKit  
**Kind**: struct

Mount options to be requested from FSKit using the `requestedMountOptions` property.

**Availability**:
- macOS 26.4+

## Declaration

```swift
struct MountOptions
```

## Topics

### Inspecting mount options
- [static var readOnly: FSVolume.MountOptions](fsvolume/mountoptions/readonly.md)
  An option to request a read-only mount.
### Working with raw values
- [init(rawValue: UInt)](fsvolume/mountoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/mountoptions)*