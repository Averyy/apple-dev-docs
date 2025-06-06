# internalError

**Framework**: Metal  
**Kind**: property

An error code that indicates the Metal framework has an internal problem.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var internalError: MTLBinaryArchiveError.Code { get }
```

#### Discussion

You can report the scenario that generated this error code with [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com).

## See Also

- [static var none: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/none.md)
  An error code that represents the absence of any problems.
- [static var invalidFile: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/invalidfile.md)
  An error code that indicates an app is using an invalid reference to an archive file, typically related to a URL.
- [static var compilationFailure: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/compilationfailure.md)
  An error code that indicates the archive’s inability to compile its contents, typically when serializing it to a URL.
- [static var unexpectedElement: MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/unexpectedelement.md)
  An error code that indicates a problem with a configuration, typically in a descriptor or an archive’s inability to add linked functions.
- [MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/code.md)
  Error codes when creating binary archives of compiled shader code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchiveerror-swift.struct/internalerror)*