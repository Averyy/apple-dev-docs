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

## See Also

- [func openItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](fsvolume/openclosehandler/openitem(_:modes:context:replyhandler:).md)
  Opens a file for access.
- [func closeItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](fsvolume/openclosehandler/closeitem(_:modes:context:replyhandler:).md)
  Closes a file from further access.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openmodes)*