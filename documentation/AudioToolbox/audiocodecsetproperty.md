# AudioCodecSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value of a codec property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecSetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

Codec properties are classified as either global properties, which remain the same for all instances of a codec, or instance properties, which may vary from instance to instance. However, not all instance property values can be modified. See [`Instance Codec Properties`](1494111-instance-codec-properties.md) for details. No property values can be modified when the codec is in the initialized state. You must call this function before you call the [`AudioCodecInitialize(_:_:_:_:_:)`](audiocodecinitialize(_:_:_:_:_:).md) function, or after you call the [`AudioCodecUninitialize(_:)`](audiocodecuninitialize(_:).md) function. Call the [`AudioCodecGetProperty(_:_:_:_:)`](audiocodecgetproperty(_:_:_:_:).md) function to retrieve the current value of a property.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions   and OpenAComponent) to obtain an audio codec object.
- `inPropertyID`: Property ID of the property whose value you want to set. Settable codec property IDs are listed in  .
- `inPropertyDataSize`: Size in bytes of the property value data.
- `inPropertyData`: Pointer to the data buffer containing the property value.

## See Also

- [func AudioCodecUninitialize(AudioCodec) -> OSStatus](audiocodecuninitialize(_:).md)
  Moves the codec from the initialized state back to the uninitialized state.
- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](audiocodecinitialize(_:_:_:_:_:).md)
  Sets up the specified codec to perform a data format translation.
- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiocodecgetproperty(_:_:_:_:).md)
  Retrieves the value of a codec property.
- [func AudioCodecGetPropertyInfo(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiocodecgetpropertyinfo(_:_:_:_:).md)
  Retrieves information about a codec property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecsetproperty(_:_:_:_:))*