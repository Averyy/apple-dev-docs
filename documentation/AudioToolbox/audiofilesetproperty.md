# AudioFileSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value of an audio file property

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileSetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ inDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAudioFile`: The audio file that you want to set a property value for.
- `inPropertyID`: The property whose value you want to set. See   for possible values. Use the   function to determine whether the property value is writable.
- `inDataSize`: The size of the value you are passing in the   parameter.
- `inPropertyData`: The new value for the property.

## See Also

- [func AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetproperty(_:_:_:_:).md)
  Gets the value of an audio file property.
- [func AudioFileGetPropertyInfo(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilegetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio file property, including the size of the property value and whether the value is writable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilesetproperty(_:_:_:_:))*