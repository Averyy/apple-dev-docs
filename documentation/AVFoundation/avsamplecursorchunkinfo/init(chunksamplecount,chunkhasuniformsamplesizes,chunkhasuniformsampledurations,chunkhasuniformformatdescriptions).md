# init(chunkSampleCount:chunkHasUniformSampleSizes:chunkHasUniformSampleDurations:chunkHasUniformFormatDescriptions:)

**Framework**: AVFoundation  
**Kind**: init

Creates a chunk information structure with the specified values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(chunkSampleCount: Int64, chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions: ObjCBool)
```

## Parameters

- `chunkSampleCount`: The count of media samples in the chunk.
- `chunkHasUniformSampleSizes`: The samples in the chunk occupy the same number of bytes in storage.
- `chunkHasUniformSampleDurations`: The samples in the chunk have the same duration.
- `chunkHasUniformFormatDescriptions`: The samples in the chunk have the same format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo/init(chunksamplecount:chunkhasuniformsamplesizes:chunkhasuniformsampledurations:chunkhasuniformformatdescriptions:))*