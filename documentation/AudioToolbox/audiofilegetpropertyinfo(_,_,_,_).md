# AudioFileGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets information about an audio file property, including the size of the property value and whether the value is writable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetPropertyInfo(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>?, _ isWritable: UnsafeMutablePointer<UInt32>?) -> OSStatus
```

```c
extern OSStatus AudioFileGetPropertyInfo(AudioFileID inAudioFile, AudioFilePropertyID inPropertyID, UInt32 *outDataSize, UInt32 *isWritable);
```

## Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFile`: The audio file you want to obtain property value information from.
- `inPropertyID`: The property whose value information you want. See [Audio File Properties](./api-1576499-audio-file-properties.md) for possible values.
- `outDataSize`: On output, the size in bytes of the property value.
- `isWritable`: On output, equals `1` if the property is writable, or `0` if it is read-only.

## See Also

### Getting and Setting Audio File Properties
- [func AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilegetproperty%28_,_,_,_%29.md)
  Gets the value of an audio file property.
- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilesetproperty%28_,_,_,_%29.md)
  Sets the value of an audio file property


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetpropertyinfo(_:_:_:_:))*