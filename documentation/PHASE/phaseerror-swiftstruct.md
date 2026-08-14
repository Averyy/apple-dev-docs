# PHASEError

**Framework**: PHASE  
**Kind**: struct

An error that PHASE reports.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct PHASEError
```

## Topics

### Identifying an Error Cause
- [static var initializeFailed: PHASEError.Code](phaseerror-swift.struct/initializefailed.md)
  An error that indicates the engine failed to initialize.
- [static var invalidObject: PHASEError.Code](phaseerror-swift.struct/invalidobject.md)
  An error that indicates an object is invalid in a specific context.
### Creating an Error
- [PHASEError.Code](phaseerror-swift.struct/code.md)
  Codes that identify errors in PHASE.
### Type Properties
- [static var errorDomain: String](phaseerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [PHASEError.Code](phaseerror-swift.struct/code.md)
  Codes that identify errors in PHASE.
- [let PHASEErrorDomain: String](phaseerrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseerror-swift.struct)*