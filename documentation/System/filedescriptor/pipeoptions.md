# FileDescriptor.PipeOptions

**Framework**: System  
**Kind**: struct

Options that specify behavior for a newly-created pipe.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct PipeOptions
```

## Topics

### Initializers
- [init(rawValue: CInt)](filedescriptor/pipeoptions/init(rawvalue:).md)
  Create a strongly-typed options value from raw C options.
### Instance Properties
- [var rawValue: CInt](filedescriptor/pipeoptions/rawvalue.md)
  The raw C options.
### Type Properties
- [static var closeOnExec: FileDescriptor.PipeOptions](filedescriptor/pipeoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var closeOnFork: FileDescriptor.PipeOptions](filedescriptor/pipeoptions/closeonfork.md)
  Indicates that forking a program closes the file.
- [static var nonBlocking: FileDescriptor.PipeOptions](filedescriptor/pipeoptions/nonblocking.md)
  Indicates that all subsequent input and output operations on the pipe’s file descriptors will be nonblocking.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipeoptions)*