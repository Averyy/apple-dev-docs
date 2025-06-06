# outOfMemory

**Framework**: PHASE  
**Kind**: property

An error the framework throws when a sound event depletes system memory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var outOfMemory: PHASESoundEventError.Code { get }
```

## See Also

- [static var apiMisuse: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/apimisuse.md)
  An error that indicates the app misconfigures data or calls the framework in unsupported succession.
- [static var badData: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/baddata.md)
  An error that indicates a sound event contains invalid data.
- [static var invalidInstance: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/invalidinstance.md)
  An error that indicates a sound event object is no longer valid.
- [static var notFound: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/notfound.md)
  An error the framework throws when it fails to find a particular sound event.
- [static var systemNotInitialized: PHASESoundEventError.Code](phasesoundeventerror-swift.struct/systemnotinitialized.md)
  An error the framework throws when engine initialization interrupts sound event playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventerror-swift.struct/outofmemory)*