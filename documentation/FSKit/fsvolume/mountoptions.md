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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/mountoptions)*