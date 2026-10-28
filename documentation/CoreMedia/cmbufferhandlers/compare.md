# compare

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

A handler callback the queue uses to perform an insertion sort of the queue.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
CMBufferCompareHandler compare;
```

## Discussion

The queue invokes this callback when enqueuing buffers to perform an insertion sort. If you don’t provide a handler, the queue defaults to FIFO order.

## See Also

### Buffer Handlers
- [typealias CMBufferCompareHandler](../cmbuffercomparehandler.md)
- [getDuration](./getduration.md)
- [getDecodeTimeStamp](./getdecodetimestamp.md)
- [getPresentationTimeStamp](./getpresentationtimestamp.md)
- [typealias CMBufferGetTimeHandler](../cmbuffergettimehandler.md)
- [getSize](./getsize.md)
- [typealias CMBufferGetSizeHandler](../cmbuffergetsizehandler.md)
- [isDataReady](./isdataready.md)
- [typealias CMBufferGetBooleanHandler](../cmbuffergetbooleanhandler.md)
- [dataBecameReadyNotification](./databecamereadynotification.md)
- [version](./version.md)
  The version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferhandlers/compare)*