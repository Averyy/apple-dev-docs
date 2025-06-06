# MTLBinaryArchiveError.Code

**Framework**: Metal  
**Kind**: enum

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

## Topics

### Error Codes
- [MTLBinaryArchiveError.Code.none](mtlbinaryarchiveerror-swift.struct/code/none.md)
  An error code that represents the absence of any problems.
- [MTLBinaryArchiveError.Code.invalidFile](mtlbinaryarchiveerror-swift.struct/code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveError.Code.compilationFailure](mtlbinaryarchiveerror-swift.struct/code/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveError.Code.unexpectedElement](mtlbinaryarchiveerror-swift.struct/code/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveError.Code.internalError](mtlbinaryarchiveerror-swift.struct/code/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLBinaryArchiveError.Code.none](mtlbinaryarchiveerror-swift.struct/code/none.md)
  An error code that represents the absence of any problems.
- [MTLBinaryArchiveError.Code.invalidFile](mtlbinaryarchiveerror-swift.struct/code/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [MTLBinaryArchiveError.Code.compilationFailure](mtlbinaryarchiveerror-swift.struct/code/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [MTLBinaryArchiveError.Code.unexpectedElement](mtlbinaryarchiveerror-swift.struct/code/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveError.Code.internalError](mtlbinaryarchiveerror-swift.struct/code/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.
### Initializers
- [init?(rawValue: UInt)](mtlbinaryarchiveerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var none: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [static var compilationFailure: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [static var unexpectedElement: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [static var internalError: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/internalerror.md)
  An error code that indicates the Metal framework has an internal problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/code)*