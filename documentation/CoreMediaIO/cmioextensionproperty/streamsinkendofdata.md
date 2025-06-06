# streamSinkEndOfData

**Framework**: Core Media I/O  
**Kind**: property

A property key for a Boolean value that indicates whether the stream has more data.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let streamSinkEndOfData: CMIOExtensionProperty
```

#### Discussion

The property state for this property is a number that represents a Boolean value: `1` indicates the stream is at its end, and `0` indicates that more data exists.

The value of this property matches the [`kCMIOStreamPropertyEndOfData`](kcmiostreampropertyendofdata.md) property.

## See Also

- [static let streamActiveFormatIndex: CMIOExtensionProperty](cmioextensionproperty/streamactiveformatindex.md)
  A property key for the index of the active stream format.
- [static let streamFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streamframeduration.md)
  A property key for the frame duration.
- [static let streamMaxFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streammaxframeduration.md)
  A property key for the maximum frame duration.
- [static let streamSinkBufferQueueSize: CMIOExtensionProperty](cmioextensionproperty/streamsinkbufferqueuesize.md)
  A property key for the sink buffer queue size.
- [static let streamSinkBuffersRequiredForStartup: CMIOExtensionProperty](cmioextensionproperty/streamsinkbuffersrequiredforstartup.md)
  A property key for the number of buffers required for startup.
- [static let streamSinkBufferUnderrunCount: CMIOExtensionProperty](cmioextensionproperty/streamsinkbufferunderruncount.md)
  A property key for the buffer underrun count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/streamsinkendofdata)*