# FSVolume.OpenModes

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Defined modes for opening a file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct OpenModes
```

```c
enum FSVolumeOpenModes : NSUInteger;
```

## Topics

### Declaring open modes
- [static var read: FSVolume.OpenModes](./openmodes/read.md)
  The read mode.
- [static var write: FSVolume.OpenModes](./openmodes/write.md)
  The write mode.
### Working with raw values
- [init(rawValue: UInt)](./openmodes/init%28rawvalue%29.md)

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

## See Also

### Opening and closing
- [func openItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](./openclosehandler/openitem%28_,modes,context,replyhandler%29.md)
  Opens a file for access.
- [func closeItem(FSItem, modes: FSVolume.OpenModes, context: FSContext, replyHandler: ((any Error)?) -> Void)](./openclosehandler/closeitem%28_,modes,context,replyhandler%29.md)
  Closes a file from further access.
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openmodes)*