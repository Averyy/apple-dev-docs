# AudioFileStreamGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFileStream`: The ID of the parser from which you wish to obtain information. The parser ID is returned by the   function.
- `inPropertyID`: A four-character ID indicating the audio file stream property about which you want information. See   for possible values.
- `outPropertyDataSize`: On output, the size, in bytes, of the current value of the specified property.
- `outWritable`: On output,   if the property can be written. Currently, there are no writable audio file stream properties.

## See Also

- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](audiofilestreamopen(_:_:_:_:_:).md)
  Creates and opens a new audio file stream parser.
- [func AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilestreamgetproperty(_:_:_:_:).md)
  Retrieves the value of the specified property.
- [func AudioFileStreamSetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilestreamsetproperty(_:_:_:_:).md)
  Sets the value of the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamgetpropertyinfo(_:_:_:_:))*