# AudioFileGetGlobalInfo(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Copies the value of a global property into a buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetGlobalInfo(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutableRawPointer?, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function can be used to get information about the capabilities of Audio File Services data types, for example, to determine which file types can take which data formats, what file types are supported, what file type can hold a particular data type, and so forth. This function cannot be used to get information about the properties of particular files. So the properties whose information you are obtaining are global to the Audio File Services programming interface, not properties specific to any file.

##### Special Considerations

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inPropertyID`: The property whose value you want to get. For possible values, see  .
- `inSpecifierSize`: The size of the specifier data.
- `inSpecifier`: A pointer to a  , which, in this context, is a pointer to a buffer containing some data that is different for each property. The type of the data required is described in the description of each property.
- `ioDataSize`: On input, a pointer to the size of the buffer specified in the outPropertyData parameter. On output, a pointer to the number of bytes written to the buffer.
- `outPropertyData`: A pointer to the buffer in which to write the property data.

## See Also

- [func AudioFileGetGlobalInfoSize(AudioFilePropertyID, UInt32, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilegetglobalinfosize(_:_:_:_:).md)
  Gets the size of a global audio file property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetglobalinfo(_:_:_:_:_:))*