# AudioFormatGetProperty(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the value of an audio format property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFormatGetProperty(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>?, _ outPropertyData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. Returns `noErr` if successful.

#### Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inPropertyID`: An   constant. For a list of these constants, see  .
- `inSpecifierSize`: The size of the specifier data.
- `inSpecifier`: A buffer of data used as an input argument for querying some of the properties.
- `ioPropertyDataSize`: On input, the size of the   buffer. On output, the number of bytes written to the buffer.
- `outPropertyData`: The buffer to write the property data to. If the   parameter is   and   is not  , the amount that would have been written is reported.

## See Also

- [func AudioFormatGetPropertyInfo(AudioFormatPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audioformatgetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio format property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioformatgetproperty(_:_:_:_:_:))*