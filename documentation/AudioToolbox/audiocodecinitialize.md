# AudioCodecInitialize(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets up the specified codec to perform a data format translation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecInitialize(_ inCodec: AudioCodec, _ inInputFormat: UnsafePointer<AudioStreamBasicDescription>?, _ inOutputFormat: UnsafePointer<AudioStreamBasicDescription>?, _ inMagicCookie: UnsafeRawPointer?, _ inMagicCookieByteSize: UInt32) -> OSStatus
```

#### Return Value

Returns `NoErr` if successful. Returns `kAudioCodecUnsupportedFormatError` if the codec cannot handle the specified data translation.  See `Result Codes` for other possible values.

#### Discussion

This function allocates any buffers needed, sets the input and output formats, and puts the codec into the initialized state. The codec has to be in the initialized state for the  [`AudioCodecAppendInputData(_:_:_:_:_:)`](audiocodecappendinputdata(_:_:_:_:_:).md) and [`AudioCodecProduceOutputPackets(_:_:_:_:_:_:)`](audiocodecproduceoutputpackets(_:_:_:_:_:_:).md) functions to work. While in this state, the format information for the translation cannot be changed; you must call the [`AudioCodecUninitialize(_:)`](audiocodecuninitialize(_:).md) function before making any changes. A codec’s properties provide information about allowable types of input and output, magic cookies, and so forth. Use the [`AudioCodecGetProperty(_:_:_:_:)`](audiocodecgetproperty(_:_:_:_:).md) function to read a codec’s properties. The properties are described in [`Global Codec Properties`](1494121-global-codec-properties.md) and [`Instance Codec Properties`](1494111-instance-codec-properties.md).

If any argument is `NULL`, any values previously set for that argument are used. For example, if you are using the same codec repeatedly with the same input and output formats, you only need to enter the formats the first time you initialize the codec. After that, you can uninitialize, change property values as necessary, and then call this function again with `NULL` in the `inInputFormat` and `inOutputFormat` parameters before processing the next set of data.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manager component instance, you can use the Component Manager (for example, the functions   and OpenAComponent) to obtain an audio codec object.
- `inInputFormat`: A structure that describes the format of the input data. See   for a description of this structure and the values of constants that can be used in this structure. If the input data has a variable number of frames per packet, this structure is supplemented with the   structure passed in the   parameter of the   function.
- `inOutputFormat`: A structure that describes the format desired for the output data.
- `inMagicCookie`: Magic cookie data, if required for the input format.
- `inMagicCookieByteSize`: Size in bytes of the magic cookie data, if any.

## See Also

- [func AudioCodecProduceOutputPackets(AudioCodec, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecproduceoutputpackets(_:_:_:_:_:_:).md)
  Retrieves output data from a codec.
- [func AudioCodecAppendInputData(AudioCodec, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](audiocodecappendinputdata(_:_:_:_:_:).md)
  Appends audio data to the codec’s input buffer.
- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiocodecgetproperty(_:_:_:_:).md)
  Retrieves the value of a codec property.
- [func AudioCodecReset(AudioCodec) -> OSStatus](audiocodecreset(_:).md)
  Flushes all the audio data in the codec and clears the input buffer.
- [func AudioCodecUninitialize(AudioCodec) -> OSStatus](audiocodecuninitialize(_:).md)
  Moves the codec from the initialized state back to the uninitialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecinitialize(_:_:_:_:_:))*