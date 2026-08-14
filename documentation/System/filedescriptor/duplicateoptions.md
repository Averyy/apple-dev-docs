# FileDescriptor.DuplicateOptions

**Framework**: System  
**Kind**: struct

Options that specify behavior for a duplicated file descriptor.

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
struct DuplicateOptions
```

## Topics

### Initializers
- [init(rawValue: CInt)](filedescriptor/duplicateoptions/init(rawvalue:).md)
  Create a strongly-typed options value from raw C options.
### Instance Properties
- [var rawValue: CInt](filedescriptor/duplicateoptions/rawvalue.md)
  The raw C options.
### Type Properties
- [static var closeOnExec: FileDescriptor.DuplicateOptions](filedescriptor/duplicateoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var closeOnFork: FileDescriptor.DuplicateOptions](filedescriptor/duplicateoptions/closeonfork.md)
  Indicates that forking a program closes the file.

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicateoptions)*