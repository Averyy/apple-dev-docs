# AudioFileStreamSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Sets the value of the specified property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamSetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileStreamSetProperty(AudioFileStreamID inAudioFileStream, AudioFileStreamPropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

## Return Value

A result code. See Result Codes.

## Discussion

Currently, there are no settable properties.

## Parameters

- `inAudioFileStream`: The ID of the parser to which you wish to pass data. The parser ID is returned by the [`AudioFileStreamOpen(_:_:_:_:_:)`](./audiofilestreamopen%28_,_,_,_,_%29.md) function.
- `inPropertyID`: The ID of the audio file stream property whose value is to be set.
- `inPropertyDataSize`: The size, in bytes, of the property data.
- `inPropertyData`: The property data.

## See Also

### Related Documentation
- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](./audiofilestreamopen%28_,_,_,_,_%29.md)
  Creates and opens a new audio file stream parser.
### Working with Data Stream Property Information
- [func AudioFileStreamGetPropertyInfo(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audiofilestreamgetpropertyinfo%28_,_,_,_%29.md)
  Retrieves information about a property value.
- [func AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilestreamgetproperty%28_,_,_,_%29.md)
  Retrieves the value of the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamsetproperty(_:_:_:_:))*