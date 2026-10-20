# AVSampleCursorDependencyInfo

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A value for describing dependencies between a media sample and other media samples in the same sample sequence.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVSampleCursorDependencyInfo
```

```c
typedef struct { ... } AVSampleCursorDependencyInfo;
```

## Topics

### Dependency information
- [var sampleIndicatesWhetherItHasDependentSamples: ObjCBool](./avsamplecursordependencyinfo/sampleindicateswhetherithasdependentsamples.md)
  A Boolean value that determines whether the sample indicates if other samples depend on it.
- [var sampleHasDependentSamples: ObjCBool](./avsamplecursordependencyinfo/samplehasdependentsamples.md)
  A Boolean value that determines whether the sample has dependent samples.
- [var sampleIndicatesWhetherItDependsOnOthers: ObjCBool](./avsamplecursordependencyinfo/sampleindicateswhetheritdependsonothers.md)
  A Boolean value that determines whether the sample indicates that it depends on other samples.
- [var sampleDependsOnOthers: ObjCBool](./avsamplecursordependencyinfo/sampledependsonothers.md)
  A Boolean value that determines whether the sample depends on other samples.
- [var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool](./avsamplecursordependencyinfo/sampleindicateswhetherithasredundantcoding.md)
  A Boolean value that determines whether the sample indicates that it has redundant coding.
- [var sampleHasRedundantCoding: ObjCBool](./avsamplecursordependencyinfo/samplehasredundantcoding.md)
  A Boolean value that determines whether the sample has redundant coding.
### Initializers
- [init()](./avsamplecursordependencyinfo/init%28%29.md)
  Creates a sample cursor dependency information structure.
- [init(sampleIndicatesWhetherItHasDependentSamples: ObjCBool, sampleHasDependentSamples: ObjCBool, sampleIndicatesWhetherItDependsOnOthers: ObjCBool, sampleDependsOnOthers: ObjCBool, sampleIndicatesWhetherItHasRedundantCoding: ObjCBool, sampleHasRedundantCoding: ObjCBool)](./avsamplecursordependencyinfo/init%28sampleindicateswhetherithasdependentsamples,samplehasdependentsamples,sampleindicateswhetheritdependsonothers,sampledependsonothers,sampleindicateswhetherithasredundantcoding,samplehasredundantcoding%29.md)
  Creates a sample cursor dependency information structure with sample information.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Sample cursors
- [class AVSampleCursor](./avsamplecursor.md)
  An object that provides information about the media sample at the cursor’s current position.
- [struct AVSampleCursorSyncInfo](./avsamplecursorsyncinfo.md)
  A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [struct AVSampleCursorAudioDependencyInfo](./avsamplecursoraudiodependencyinfo.md)
  A structure that describes the independent decodability of audio samples.
- [struct AVSampleCursorStorageRange](./avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.
- [struct AVSampleCursorChunkInfo](./avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo)*