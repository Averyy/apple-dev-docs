# invalidInstance

**Framework**: PHASE  
**Kind**: property

An error that indicates a sound event object is no longer valid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var invalidInstance: PHASESoundEventError.Code { get }
```

## See Also

- [static var apiMisuse: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [static var badData: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/baddata.md)
  An error that indicates a sound event contains invalid data.
- [static var notFound: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [static var outOfMemory: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/outofmemory.md)
  An error the framework throws when a sound event depletes system memory.
- [static var systemNotInitialized: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/systemnotinitialized.md)
  An error the framework throws when engine initialization interrupts sound event playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct/invalidinstance)*