# chunkSampleCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The count of media samples in the chunk.

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
var chunkSampleCount: Int64
```

```c
int64_t chunkSampleCount;
```

## See Also

### Chunk information
- [var chunkHasUniformSampleSizes: ObjCBool](./chunkhasuniformsamplesizes.md)
  The samples in the chunk occupy the same number of bytes in storage.
- [var chunkHasUniformSampleDurations: ObjCBool](./chunkhasuniformsampledurations.md)
  The samples in the chunk have the same duration.
- [var chunkHasUniformFormatDescriptions: ObjCBool](./chunkhasuniformformatdescriptions.md)
  The samples in the chunk have the same format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo/chunksamplecount)*