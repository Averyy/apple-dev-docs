# sinkBufferQueueSize

**Framework**: Core Media I/O  
**Kind**: property

The buffer queue size.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var sinkBufferQueueSize: Int? { get set }
```

#### Discussion

This property translates to the [`kCMIOStreamPropertyOutputBufferQueueSize`](kcmiostreampropertyoutputbufferqueuesize.md) property.

## See Also

- [var sinkBuffersRequiredForStartup: Int?](cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq.md)
  The number of buffers the stream requires for startup.
- [var sinkBufferUnderrunCount: Int?](cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb.md)
  The buffer underrun count.
- [var sinkEndOfData: Int?](cmioextensionstreamproperties/sinkendofdata-8fswu.md)
  A value that indicates whether the stream has reached its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkbufferqueuesize-9b80c)*