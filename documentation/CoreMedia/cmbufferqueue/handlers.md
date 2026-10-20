# CMBufferQueue.Handlers

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Handlers
```

## Topics

### Initializers
- [init(withHandlers: (inout CMBufferQueue.Handlers.Builder) -> Void)](./handlers/init%28withhandlers%29.md)
### Instance Properties
- [let compare: CMBufferCompareHandler?](./handlers/compare.md)
- [let dataBecameReadyNotification: String?](./handlers/databecamereadynotification.md)
- [let getDecodeTimeStamp: CMBufferGetTimeHandler?](./handlers/getdecodetimestamp.md)
- [let getDuration: CMBufferGetTimeHandler](./handlers/getduration.md)
- [let getPresentationTimeStamp: CMBufferGetTimeHandler?](./handlers/getpresentationtimestamp.md)
- [let getSize: CMBufferGetSizeHandler?](./handlers/getsize.md)
- [let isDataReady: CMBufferGetBooleanHandler?](./handlers/isdataready.md)
### Type Properties
- [static let outputPTSSortedSampleBuffers: CMBufferQueue.Handlers](./handlers/outputptssortedsamplebuffers.md)
- [static let unsortedSampleBuffers: CMBufferQueue.Handlers](./handlers/unsortedsamplebuffers.md)
### Instance Methods
- [func withHandlers((inout CMBufferQueue.Handlers.Builder) -> Void) -> CMBufferQueue.Handlers](./handlers/withhandlers%28_%29.md)
### Structures
- [CMBufferQueue.Handlers.Builder](./handlers/builder.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Data Types
- [CMBufferQueue.Buffers](./buffers-swift.struct.md)
  A sequence of `CMBuffer`s.
- [CMBufferQueue.Error](./error.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/handlers)*