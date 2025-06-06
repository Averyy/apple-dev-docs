# sinkBufferUnderrunCount

**Framework**: Core Media I/O  
**Kind**: property

The buffer underrun count.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var sinkBufferUnderrunCount: Int? { get set }
```

#### Discussion

This value is a number the system increments whenever you’re not servicing buffers fast enough.

This property translates to the [`kCMIOStreamPropertyOutputBufferUnderrunCount`](kcmiostreampropertyoutputbufferunderruncount.md) property.

## See Also

- [var sinkBufferQueueSize: Int?](cmioextensionstreamproperties/sinkbufferqueuesize-9b80c.md)
  The buffer queue size.
- [var sinkBuffersRequiredForStartup: Int?](cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq.md)
  The number of buffers the stream requires for startup.
- [var sinkEndOfData: Int?](cmioextensionstreamproperties/sinkendofdata-8fswu.md)
  A value that indicates whether the stream has reached its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb)*