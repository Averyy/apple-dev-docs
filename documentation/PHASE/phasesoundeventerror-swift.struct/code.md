# PHASESoundEventError.Code

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Codes that identify sound event errors.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum PHASESoundEventError : NSInteger;
```

## Topics

### Errors
- [PHASESoundEventError.Code.apiMisuse](./code/apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [PHASESoundEventError.Code.badData](./code/baddata.md)
  An error that indicates a sound event contains invalid data.
- [PHASESoundEventError.Code.invalidInstance](./code/invalidinstance.md)
  An error that indicates a sound event object is no longer valid.
- [PHASESoundEventError.Code.notFound](./code/notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [PHASESoundEventError.Code.outOfMemory](./code/outofmemory.md)
  An error the framework throws when a sound event depletes system memory.
- [PHASESoundEventError.Code.systemNotInitialized](./code/systemnotinitialized.md)
  An error the framework throws when engine initialization interrupts sound event playback.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sound Event Errors
- [struct PHASESoundEventError](../phasesoundeventerror-swift.struct.md)
  A sound event error that PHASE reports.
- [let PHASESoundEventErrorDomain: String](../phasesoundeventerrordomain.md)
  A unique error domain for sound events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct/code)*