# AudioConverterGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets an audio converter property value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterGetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inAudioConverter`: The audio converter to get a property value from.
- `inPropertyID`: The property whose value you want.
- `ioPropertyDataSize`: On input, the size of the memory pointed to by the   parameter. On output, the size of the property value.
- `outPropertyData`: On output, the property value you wanted to get.

## See Also

- [func AudioConverterGetPropertyInfo(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioconvertergetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio converter property.
- [func AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audioconvertersetproperty(_:_:_:_:).md)
  Sets the value of an audio converter object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertergetproperty(_:_:_:_:))*