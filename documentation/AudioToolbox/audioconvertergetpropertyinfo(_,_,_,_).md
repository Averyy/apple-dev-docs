# AudioConverterGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioConverterGetPropertyInfo(AudioConverterRef inAudioConverter, AudioConverterPropertyID inPropertyID, UInt32 *outSize, Boolean *outWritable);
```

## Return Value

A  result code.

## Parameters

- `inAudioConverter`: The audio converter to get property information from.
- `inPropertyID`: The property you want information about.
- `outSize`: On output, the size of the property value in bytes. Can be `NULL` on output.
- `outWritable`: On output, a Boolean value indicating whether the property value is writable (`true`) or not (`false`). Can be `NULL` on output.

## See Also

### Configuring Audio Converter Properties
- [func AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audioconvertergetproperty%28_,_,_,_%29.md)
  Gets an audio converter property value.
- [func AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audioconvertersetproperty%28_,_,_,_%29.md)
  Sets the value of an audio converter object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertergetpropertyinfo(_:_:_:_:))*