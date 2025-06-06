# sinkBuffersRequiredForStartup

**Framework**: Core Media I/O  
**Kind**: property

The number of buffers the stream requires for startup.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var sinkBuffersRequiredForStartup: Int? { get set }
```

#### Discussion

This property translates to the [`kCMIOStreamPropertyOutputBuffersRequiredForStartup`](kcmiostreampropertyoutputbuffersrequiredforstartup.md) property.

## See Also

- [var sinkBufferQueueSize: Int?](cmioextensionstreamproperties/sinkbufferqueuesize-9b80c.md)
  The buffer queue size.
- [var sinkBufferUnderrunCount: Int?](cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb.md)
  The buffer underrun count.
- [var sinkEndOfData: Int?](cmioextensionstreamproperties/sinkendofdata-8fswu.md)
  A value that indicates whether the stream has reached its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq)*