# AudioCodecSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioCodecSetProperty(AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

Codec properties are classified as either global properties, which remain the same for all instances of a codec, or instance properties, which may vary from instance to instance. However, not all instance property values can be modified. See [Instance Codec Properties](./api-1494111-instance-codec-properties.md) for details. No property values can be modified when the codec is in the initialized state. You must call this function before you call the [`AudioCodecInitialize(_:_:_:_:_:)`](./audiocodecinitialize%28_,_,_,_,_%29.md) function, or after you call the [`AudioCodecUninitialize(_:)`](./audiocodecuninitialize%28_%29.md) function. Call the [`AudioCodecGetProperty(_:_:_:_:)`](./audiocodecgetproperty%28_,_,_,_%29.md) function to retrieve the current value of a property.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions [`FindNextComponent`](../coreservices/api-1516552-findnextcomponent.md) and OpenAComponent) to obtain an audio codec object.
- `inPropertyID`: Property ID of the property whose value you want to set. Settable codec property IDs are listed in [Instance Codec Properties](./api-1494111-instance-codec-properties.md).
- `inPropertyDataSize`: Size in bytes of the property value data.
- `inPropertyData`: Pointer to the data buffer containing the property value.

## See Also

### Related Documentation
- [func AudioCodecUninitialize(AudioCodec) -> OSStatus](./audiocodecuninitialize%28_%29.md)
  Moves the codec from the initialized state back to the uninitialized state.
- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](./audiocodecinitialize%28_,_,_,_,_%29.md)
  Sets up the specified codec to perform a data format translation.
### Accessing Codec Properties
- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiocodecgetproperty%28_,_,_,_%29.md)
  Retrieves the value of a codec property.
- [func AudioCodecGetPropertyInfo(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audiocodecgetpropertyinfo%28_,_,_,_%29.md)
  Retrieves information about a codec property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecsetproperty(_:_:_:_:))*