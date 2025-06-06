# AudioFileStream_PacketsProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Invoked by an audio file stream parser when it finds audio data in the audio file stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioFileStream_PacketsProc = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeRawPointer, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> Void
```

#### Discussion

If you named your function `MyAudioFileStream_PacketsProc`, you would declare it like this:

##### Discussion

For constant-bit-rate (CBR) audio data, your callback is typically called with as much data as you passed to the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function. At times, however, only a single packet might be passed because of boundaries in the input data. For variable-bit-rate (VBR) audio data, your callback might be called several times for each time you called the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function.

## Parameters

- `inClientData`: The value you provided in the   parameter when you called the   function.
- `inNumberBytes`: The number of bytes of data in the   buffer.
- `inNumberPackets`: The number of packets of audio data in the   buffer.
- `inInputData`: The audio data.
- `inPacketDescriptions`: An array of audio file stream packet description structures describing the data. Audio file stream packet description structures are described in  .

## See Also

- [typealias AudioFileStream_PropertyListenerProc](audiofilestream_propertylistenerproc.md)
  Invoked by an audio file stream parser when it finds a property value in the audio file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_packetsproc)*