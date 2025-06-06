# AudioFileGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the value of an audio file property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inAudioFile`: The audio file you want to obtain a property value from.
- `inPropertyID`: The property whose value you want. See   for possible values.
- `ioDataSize`: On input, the size of the buffer passed in the   parameter. On output, the number of bytes written to the buffer. Use the   function to obtain the size of the property value.
- `outPropertyData`: On output, the value of the property specified in the   parameter.

## See Also

- [func AudioFileGetPropertyInfo(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilegetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio file property, including the size of the property value and whether the value is writable.
- [func AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetproperty(_:_:_:_:).md)
  Sets the value of an audio file property


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetproperty(_:_:_:_:))*