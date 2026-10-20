# FileDescriptor.PipeOptions

**Framework**: System  
**Kind**: struct  
**Role**: Structure

Options that specify behavior for a newly-created pipe.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct PipeOptions
```

## Topics

### Initializers
- [init(rawValue: CInt)](./pipeoptions/init%28rawvalue%29.md)
  Create a strongly-typed options value from raw C options.
### Instance Properties
- [var rawValue: CInt](./pipeoptions/rawvalue.md)
  The raw C options.
### Type Properties
- [static var closeOnExec: FileDescriptor.PipeOptions](./pipeoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var closeOnFork: FileDescriptor.PipeOptions](./pipeoptions/closeonfork.md)
  Indicates that forking a program closes the file.
- [static var nonBlocking: FileDescriptor.PipeOptions](./pipeoptions/nonblocking.md)
  Indicates that all subsequent input and output operations on the pipe’s file descriptors will be nonblocking.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipeoptions)*