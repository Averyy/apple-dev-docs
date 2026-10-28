# AudioFileStream_PacketsProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Invoked by an audio file stream parser when it finds audio data in the audio file stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioFileStream_PacketsProc = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeRawPointer, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> Void
```

```c
typedef void (*)(void *, unsigned int, unsigned int, const void *, struct AudioStreamPacketDescription *) AudioFileStream_PacketsProc;
```

## Discussion

If you named your function `MyAudioFileStream_PacketsProc`, you would declare it like this:

### Discussion

For constant-bit-rate (CBR) audio data, your callback is typically called with as much data as you passed to the [`AudioFileStreamParseBytes(_:_:_:_:)`](./audiofilestreamparsebytes%28_,_,_,_%29.md) function. At times, however, only a single packet might be passed because of boundaries in the input data. For variable-bit-rate (VBR) audio data, your callback might be called several times for each time you called the [`AudioFileStreamParseBytes(_:_:_:_:)`](./audiofilestreamparsebytes%28_,_,_,_%29.md) function.

## Parameters

- `inClientData`: The value you provided in the `inClientData` parameter when you called the [`AudioFileStreamOpen(_:_:_:_:_:)`](./audiofilestreamopen%28_,_,_,_,_%29.md) function.
- `inNumberBytes`: The number of bytes of data in the `inInputData` buffer.
- `inNumberPackets`: The number of packets of audio data in the `inInputData` buffer.
- `inInputData`: The audio data.
- `inPacketDescriptions`: An array of audio file stream packet description structures describing the data. Audio file stream packet description structures are described in [Core Audio Data Types](../CoreAudio/core-audio-data-types.md).

## See Also

### Callbacks
- [typealias AudioFileStream_PropertyListenerProc](./audiofilestream_propertylistenerproc.md)
  Invoked by an audio file stream parser when it finds a property value in the audio file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_packetsproc)*