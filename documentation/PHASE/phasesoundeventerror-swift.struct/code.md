# PHASESoundEventError.Code

**Framework**: PHASE  
**Kind**: enum

Codes that identify sound event errors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Code
```

## Topics

### Errors
- [PHASESoundEventError.Code.apiMisuse](phasesoundeventerror-swift.struct/code/apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [PHASESoundEventError.Code.badData](phasesoundeventerror-swift.struct/code/baddata.md)
  An error that indicates a sound event contains invalid data.
- [PHASESoundEventError.Code.invalidInstance](phasesoundeventerror-swift.struct/code/invalidinstance.md)
  An error that indicates a sound event object is no longer valid.
- [PHASESoundEventError.Code.notFound](phasesoundeventerror-swift.struct/code/notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [PHASESoundEventError.Code.outOfMemory](phasesoundeventerror-swift.struct/code/outofmemory.md)
  An error the framework throws when a sound event depletes system memory.
- [PHASESoundEventError.Code.systemNotInitialized](phasesoundeventerror-swift.struct/code/systemnotinitialized.md)
  An error the framework throws when engine initialization interrupts sound event playback.
### Initializers
- [init?(rawValue: Int)](phasesoundeventerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PHASESoundEventError](phasesoundeventerror-swift.struct.md)
  A sound event error that PHASE reports.
- [let PHASESoundEventErrorDomain: String](phasesoundeventerrordomain.md)
  A unique error domain for sound events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct/code)*