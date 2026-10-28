# streamFrameDuration

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Type Property

A property key for the frame duration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let streamFrameDuration: CMIOExtensionProperty
```

```c
extern CMIOExtensionProperty const CMIOExtensionPropertyStreamFrameDuration;
```

## Discussion

The property state for this property is a dictionary that represents a [`CMTime`](../../CoreMedia/cmtime.md) value that matches the frame duration of the active stream format.

## See Also

### Stream Properties
- [static let streamActiveFormatIndex: CMIOExtensionProperty](./streamactiveformatindex.md)
  A property key for the index of the active stream format.
- [static let streamMaxFrameDuration: CMIOExtensionProperty](./streammaxframeduration.md)
  A property key for the maximum frame duration.
- [static let streamSinkBufferQueueSize: CMIOExtensionProperty](./streamsinkbufferqueuesize.md)
  A property key for the sink buffer queue size.
- [static let streamSinkBuffersRequiredForStartup: CMIOExtensionProperty](./streamsinkbuffersrequiredforstartup.md)
  A property key for the number of buffers required for startup.
- [static let streamSinkBufferUnderrunCount: CMIOExtensionProperty](./streamsinkbufferunderruncount.md)
  A property key for the buffer underrun count.
- [static let streamSinkEndOfData: CMIOExtensionProperty](./streamsinkendofdata.md)
  A property key for a Boolean value that indicates whether the stream has more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/streamframeduration)*