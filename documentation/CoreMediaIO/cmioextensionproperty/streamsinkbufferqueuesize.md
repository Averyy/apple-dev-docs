# streamSinkBufferQueueSize

**Framework**: Core Media I/O  
**Kind**: property

A property key for the sink buffer queue size.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let streamSinkBufferQueueSize: CMIOExtensionProperty
```

#### Discussion

The property state for this property is a number. The property value matches the value of the [`kCMIOStreamPropertyOutputBufferQueueSize`](kcmiostreampropertyoutputbufferqueuesize.md) property.

## See Also

- [static let streamActiveFormatIndex: CMIOExtensionProperty](cmioextensionproperty/streamactiveformatindex.md)
  A property key for the index of the active stream format.
- [static let streamFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streamframeduration.md)
  A property key for the frame duration.
- [static let streamMaxFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streammaxframeduration.md)
  A property key for the maximum frame duration.
- [static let streamSinkBuffersRequiredForStartup: CMIOExtensionProperty](cmioextensionproperty/streamsinkbuffersrequiredforstartup.md)
  A property key for the number of buffers required for startup.
- [static let streamSinkBufferUnderrunCount: CMIOExtensionProperty](cmioextensionproperty/streamsinkbufferunderruncount.md)
  A property key for the buffer underrun count.
- [static let streamSinkEndOfData: CMIOExtensionProperty](cmioextensionproperty/streamsinkendofdata.md)
  A property key for a Boolean value that indicates whether the stream has more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/streamsinkbufferqueuesize)*