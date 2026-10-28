# AudioFileStreamGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Retrieves information about a property value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

```c
extern OSStatus AudioFileStreamGetPropertyInfo(AudioFileStreamID inAudioFileStream, AudioFileStreamPropertyID inPropertyID, UInt32 *outPropertyDataSize, Boolean *outWritable);
```

## Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFileStream`: The ID of the parser from which you wish to obtain information. The parser ID is returned by the [`AudioFileStreamOpen(_:_:_:_:_:)`](./audiofilestreamopen%28_,_,_,_,_%29.md) function.
- `inPropertyID`: A four-character ID indicating the audio file stream property about which you want information. See [Audio File Stream Properties](./api-1391506-audio-file-stream-properties.md) for possible values.
- `outPropertyDataSize`: On output, the size, in bytes, of the current value of the specified property.
- `outWritable`: On output, `true` if the property can be written. Currently, there are no writable audio file stream properties.

## See Also

### Related Documentation
- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](./audiofilestreamopen%28_,_,_,_,_%29.md)
  Creates and opens a new audio file stream parser.
### Working with Data Stream Property Information
- [func AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilestreamgetproperty%28_,_,_,_%29.md)
  Retrieves the value of the specified property.
- [func AudioFileStreamSetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilestreamsetproperty%28_,_,_,_%29.md)
  Sets the value of the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamgetpropertyinfo(_:_:_:_:))*