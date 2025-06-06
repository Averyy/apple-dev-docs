# AudioCodecGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Retrieves information about a codec property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecGetPropertyInfo(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

Call this function to:

- get the size of a property value before calling [`AudioCodecGetProperty(_:_:_:_:)`](audiocodecgetproperty(_:_:_:_:).md) to retrieve the value
- find out if a property value can be modified before calling [`AudioCodecSetProperty(_:_:_:_:)`](audiocodecsetproperty(_:_:_:_:).md) to set the value

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions   and OpenAComponent) to obtain an audio codec object.
- `inPropertyID`: Property ID of the property about which you want to obtain information. Codec property IDs are listed in   and  .
- `outSize`: On return, size in bytes of the current value of the property.
- `outWritable`: Returns   if you can change the value of the property, otherwise  .

## See Also

- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiocodecgetproperty(_:_:_:_:).md)
  Retrieves the value of a codec property.
- [func AudioCodecSetProperty(AudioCodec, AudioCodecPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiocodecsetproperty(_:_:_:_:).md)
  Sets the value of a codec property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyinfo(_:_:_:_:))*