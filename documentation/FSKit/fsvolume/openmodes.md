# FSVolume.OpenModes

**Framework**: FSKit  
**Kind**: struct

Defined modes for opening a file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct OpenModes
```

## Topics

### Declaring open modes
- [static var read: FSVolume.OpenModes](fsvolume/openmodes/read.md)
  The read mode.
- [static var write: FSVolume.OpenModes](fsvolume/openmodes/write.md)
  The write mode.
### Working with raw values
- [init(rawValue: UInt)](fsvolume/openmodes/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsvolume/openmodes/equatable-implementations.md)
- [OptionSet Implementations](fsvolume/openmodes/optionset-implementations.md)
- [SetAlgebra Implementations](fsvolume/openmodes/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func openItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](fsvolume/opencloseoperations/openitem(_:modes:replyhandler:).md)
  Opens a file for access.
- [func closeItem(FSItem, modes: FSVolume.OpenModes, replyHandler: ((any Error)?) -> Void)](fsvolume/opencloseoperations/closeitem(_:modes:replyhandler:).md)
  Closes a file from further access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openmodes)*