# systemNotInitialized

**Framework**: PHASE  
**Kind**: property  
**Role**: Type Property

An error the framework throws when engine initialization interrupts sound event playback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var systemNotInitialized: PHASESoundEventError.Code { get }
```

## See Also

### Identifying an Error Cause
- [static var apiMisuse: PHASESoundEventError.Code](./apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [static var badData: PHASESoundEventError.Code](./baddata.md)
  An error that indicates a sound event contains invalid data.
- [static var invalidInstance: PHASESoundEventError.Code](./invalidinstance.md)
  An error that indicates a sound event object is no longer valid.
- [static var notFound: PHASESoundEventError.Code](./notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [static var outOfMemory: PHASESoundEventError.Code](./outofmemory.md)
  An error the framework throws when a sound event depletes system memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct/systemnotinitialized)*