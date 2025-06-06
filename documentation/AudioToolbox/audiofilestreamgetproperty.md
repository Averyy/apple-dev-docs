# AudioFileStreamGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Retrieves the value of the specified property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamGetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inAudioFileStream`: The ID of the parser from which you wish to obtain data. The parser ID is returned by the   function.
- `inPropertyID`: A four-character ID indicating the audio file stream property whose value you want to read. See   for possible values.
- `ioPropertyDataSize`: On input, the size of the buffer in the   parameter. Call the   function to obtain the size of the property value. On output, the number of bytes of the property value returned.
- `outPropertyData`: On output, the value of the specified property.

## See Also

- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](audiofilestreamopen(_:_:_:_:_:).md)
  Creates and opens a new audio file stream parser.
- [func AudioFileStreamGetPropertyInfo(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiofilestreamgetpropertyinfo(_:_:_:_:).md)
  Retrieves information about a property value.
- [func AudioFileStreamSetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilestreamsetproperty(_:_:_:_:).md)
  Sets the value of the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamgetproperty(_:_:_:_:))*