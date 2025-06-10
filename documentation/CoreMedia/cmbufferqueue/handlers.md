# CMBufferQueue.Handlers

**Framework**: Core Media  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
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
- [init(withHandlers: (inout CMBufferQueue.Handlers.Builder) -> Void)](cmbufferqueue/handlers/init(withhandlers:).md)
### Instance Properties
- [let compare: CMBufferCompareHandler?](cmbufferqueue/handlers/compare.md)
- [let dataBecameReadyNotification: String?](cmbufferqueue/handlers/databecamereadynotification.md)
- [let getDecodeTimeStamp: CMBufferGetTimeHandler?](cmbufferqueue/handlers/getdecodetimestamp.md)
- [let getDuration: CMBufferGetTimeHandler](cmbufferqueue/handlers/getduration.md)
- [let getPresentationTimeStamp: CMBufferGetTimeHandler?](cmbufferqueue/handlers/getpresentationtimestamp.md)
- [let getSize: CMBufferGetSizeHandler?](cmbufferqueue/handlers/getsize.md)
- [let isDataReady: CMBufferGetBooleanHandler?](cmbufferqueue/handlers/isdataready.md)
### Type Properties
- [static let outputPTSSortedSampleBuffers: CMBufferQueue.Handlers](cmbufferqueue/handlers/outputptssortedsamplebuffers.md)
- [static let unsortedSampleBuffers: CMBufferQueue.Handlers](cmbufferqueue/handlers/unsortedsamplebuffers.md)
### Instance Methods
- [func withHandlers((inout CMBufferQueue.Handlers.Builder) -> Void) -> CMBufferQueue.Handlers](cmbufferqueue/handlers/withhandlers(_:).md)
### Structures
- [CMBufferQueue.Handlers.Builder](cmbufferqueue/handlers/builder.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CMBufferQueue.Buffers](cmbufferqueue/buffers-swift.struct.md)
- [CMBufferQueue.Error](cmbufferqueue/error.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/handlers)*