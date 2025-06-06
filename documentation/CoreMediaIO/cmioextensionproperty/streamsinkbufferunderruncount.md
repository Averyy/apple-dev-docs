# streamSinkBufferUnderrunCount

**Framework**: Core Media I/O  
**Kind**: property

A property key for the buffer underrun count.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let streamSinkBufferUnderrunCount: CMIOExtensionProperty
```

#### Discussion

The system updates this value every time you don’t service a stream’s buffer fast enough.

The property state for property is a number with a read-only attribute. The value of this property matches the value of the [`kCMIOStreamPropertyOutputBufferUnderrunCount`](kcmiostreampropertyoutputbufferunderruncount.md) property.

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
- [static let streamSinkEndOfData: CMIOExtensionProperty](cmioextensionproperty/streamsinkendofdata.md)
  A property key for a Boolean value that indicates whether the stream has more data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/streamsinkbufferunderruncount)*