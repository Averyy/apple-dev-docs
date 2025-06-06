# sinkEndOfData

**Framework**: Core Media I/O  
**Kind**: property

A value that indicates whether the stream has reached its end.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var sinkEndOfData: Int? { get set }
```

#### Discussion

A value of `1` indicates that the stream has reached the end, and a value of `0` indicates that more data is available. This property translates to the [`kCMIOStreamPropertyEndOfData`](kcmiostreampropertyendofdata.md) property.

## See Also

- [var sinkBufferQueueSize: Int?](cmioextensionstreamproperties/sinkbufferqueuesize-9b80c.md)
  The buffer queue size.
- [var sinkBuffersRequiredForStartup: Int?](cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq.md)
  The number of buffers the stream requires for startup.
- [var sinkBufferUnderrunCount: Int?](cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb.md)
  The buffer underrun count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkendofdata-8fswu)*