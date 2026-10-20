# AudioCodecGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Retrieves the value of a codec property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecGetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioCodecGetProperty(AudioCodec inCodec, AudioCodecPropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

All property values can be read regardless of the state of the codec. However, the values of some properties depend on whether the codec is initialized. Before calling this function, call the [`AudioCodecGetPropertyInfo(_:_:_:_:)`](./audiocodecgetpropertyinfo%28_,_,_,_%29.md) function to determine the size of buffer you need for the property value.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions [`FindNextComponent`](../coreservices/api-1516552-findnextcomponent.md) and OpenAComponent) to obtain an audio codec object.
- `inPropertyID`: Property ID of the property whose value you want to obtain. Codec property IDs are listed in [Global Codec Properties](./api-1494121-global-codec-properties.md) and [Instance Codec Properties](./api-1494111-instance-codec-properties.md).
- `ioPropertyDataSize`: On input, the size in bytes of the data buffer pointed to by the `outPropertyData` parameter. On output, the amount of data actually written to the buffer.
- `outPropertyData`: The property data buffer.

## See Also

### Accessing Codec Properties
- [func AudioCodecGetPropertyInfo(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audiocodecgetpropertyinfo%28_,_,_,_%29.md)
  Retrieves information about a codec property.
- [func AudioCodecSetProperty(AudioCodec, AudioCodecPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiocodecsetproperty%28_,_,_,_%29.md)
  Sets the value of a codec property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetproperty(_:_:_:_:))*