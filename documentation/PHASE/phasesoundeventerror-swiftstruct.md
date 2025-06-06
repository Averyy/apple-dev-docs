# PHASESoundEventError

**Framework**: PHASE  
**Kind**: struct

A sound event error that PHASE reports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct PHASESoundEventError
```

## Topics

### Creating an Error
- [PHASESoundEventError.Code](phasesoundeventerror-swift.struct/code.md)
  Codes that identify sound event errors.
### Identifying an Error Cause
- [static var apiMisuse: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [static var badData: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/baddata.md)
  An error that indicates a sound event contains invalid data.
- [static var invalidInstance: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/invalidinstance.md)
  An error that indicates a sound event object is no longer valid.
- [static var notFound: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [static var outOfMemory: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/outofmemory.md)
  An error the framework throws when a sound event depletes system memory.
- [static var systemNotInitialized: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/systemnotinitialized.md)
  An error the framework throws when engine initialization interrupts sound event playback.
### Type Properties
- [static var errorDomain: String](phasesoundeventerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [PHASESoundEventError.Code](phasesoundeventerror-swift.struct/code.md)
  Codes that identify sound event errors.
- [let PHASESoundEventErrorDomain: String](phasesoundeventerrordomain.md)
  A unique error domain for sound events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct)*