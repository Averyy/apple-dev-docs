# AudioConverterSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value of an audio converter object property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterSetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

You can employ the property mechanism, for example, to split a monaural input to both channels of a stereo output. You would do this as follows:

```objc
 SInt32 channelMap[2] = {0, 0}; // array size should match the number of output channels
 AudioConverterSetProperty (
    theConverter,
    kAudioConverterChannelMap,
    sizeof(channelMap),
    channelMap
);
```

## Parameters

- `inAudioConverter`: The audio converter to set a property value on.
- `inPropertyID`: The property whose value you want to set.
- `inPropertyDataSize`: The size, in bytes, of the property value.
- `inPropertyData`: The value you want to apply to the specified property.

## See Also

- [func AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconvertergetproperty(_:_:_:_:).md)
  Gets an audio converter property value.
- [func AudioConverterGetPropertyInfo(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioconvertergetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio converter property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertersetproperty(_:_:_:_:))*