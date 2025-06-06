# AudioConverterGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets information about an audio converter property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

A  result code.

## Parameters

- `inAudioConverter`: The audio converter to get property information from.
- `inPropertyID`: The property you want information about.
- `outSize`: On output, the size of the property value in bytes. Can be   on output.
- `outWritable`: On output, a Boolean value indicating whether the property value is writable ( ) or not ( ). Can be   on output.

## See Also

- [func AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconvertergetproperty(_:_:_:_:).md)
  Gets an audio converter property value.
- [func AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audioconvertersetproperty(_:_:_:_:).md)
  Sets the value of an audio converter object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertergetpropertyinfo(_:_:_:_:))*