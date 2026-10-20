# MTLBinaryArchiveError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Error codes when creating binary archives of compiled shader code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum MTLBinaryArchiveError : NSUInteger;
```

## Topics

### Error codes
- [MTLBinaryArchiveError.Code.none](./code/none.md)
  An error code that represents the absence of any problems.
- [MTLBinaryArchiveError.Code.invalidFile](./code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveError.Code.compilationFailure](./code/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveError.Code.unexpectedElement](./code/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveError.Code.internalError](./code/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLBinaryArchiveError.Code.none](./code/none.md)
  An error code that represents the absence of any problems.
- [MTLBinaryArchiveError.Code.invalidFile](./code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveError.Code.compilationFailure](./code/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveError.Code.unexpectedElement](./code/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveError.Code.internalError](./code/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.
### Initializers
- [init?(rawValue: UInt)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error codes
- [static var none: MTLBinaryArchiveError.Code](./none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLBinaryArchiveError.Code](./invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [static var compilationFailure: MTLBinaryArchiveError.Code](./compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [static var unexpectedElement: MTLBinaryArchiveError.Code](./unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [static var internalError: MTLBinaryArchiveError.Code](./internalerror.md)
  An error code that indicates the Metal framework has an internal problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/code)*