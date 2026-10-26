# sinkBuffersRequiredForStartup

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The number of buffers the stream requires for startup.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
@property (atomic, strong, nullable) NSNumber * sinkBuffersRequiredForStartup;
```

#### Discussion

This property translates to the [`kCMIOStreamPropertyOutputBuffersRequiredForStartup`](../kcmiostreampropertyoutputbuffersrequiredforstartup.md) property.

## See Also

### Configuring Sink Properties
- [sinkBufferQueueSize](./sinkbufferqueuesize-4kpug.md)
  The buffer queue size.
- [sinkBufferUnderrunCount](./sinkbufferunderruncount-9sph5.md)
  The buffer underrun count.
- [sinkEndOfData](./sinkendofdata-30he9.md)
  A value that indicates whether the stream has reached its end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/sinkbuffersrequiredforstartup-4b5te)*