# sinkBufferQueueSize

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The buffer queue size.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
@property (atomic, strong, nullable) NSNumber * sinkBufferQueueSize;
```

#### Discussion

This property translates to the [`kCMIOStreamPropertyOutputBufferQueueSize`](../kcmiostreampropertyoutputbufferqueuesize.md) property.

## See Also

### Configuring Sink Properties
- [sinkBuffersRequiredForStartup](./sinkbuffersrequiredforstartup-4b5te.md)
  The number of buffers the stream requires for startup.
- [sinkBufferUnderrunCount](./sinkbufferunderruncount-9sph5.md)
  The buffer underrun count.
- [sinkEndOfData](./sinkendofdata-30he9.md)
  A value that indicates whether the stream has reached its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkbufferqueuesize-4kpug)*