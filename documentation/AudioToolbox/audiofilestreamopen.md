# AudioFileStreamOpen(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates and opens a new audio file stream parser.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamOpen(_ inClientData: UnsafeMutableRawPointer?, _ inPropertyListenerProc: AudioFileStream_PropertyListenerProc, _ inPacketsProc: AudioFileStream_PacketsProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFileStream: UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inClientData`: A pointer to a value or structure to be passed to your callback functions.
- `inPropertyListenerProc`: Your property-listener callback. Whenever the parser finds the value of a property in the data stream, it calls your property listener with the property ID. You can then call the   and   functions to get the value of the property.
- `inPacketsProc`: Your audio-data callback. Whenever the parser finds audio data packets in the data stream, it passes the data to your audio-data callback.
- `inFileTypeHint`: If you do not know the audio file type, pass  .
- `outAudioFileStream`: On output, an opaque object representing the audio file stream parser. This object is referred to in this document as the audio file stream parser ID. You need to pass this ID in to other functions in the Audio File Stream API.

## See Also

- [func AudioFileStreamGetPropertyInfo(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiofilestreamgetpropertyinfo(_:_:_:_:).md)
  Retrieves information about a property value.
- [typealias AudioFileStream_PropertyListenerProc](audiofilestream_propertylistenerproc.md)
  Invoked by an audio file stream parser when it finds a property value in the audio file stream.
- [func AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilestreamgetproperty(_:_:_:_:).md)
  Retrieves the value of the specified property.
- [typealias AudioFileStream_PacketsProc](audiofilestream_packetsproc.md)
  Invoked by an audio file stream parser when it finds audio data in the audio file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamopen(_:_:_:_:_:))*