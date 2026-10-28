# ExtAudioFileGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets a property value from an extended audio file object.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileGetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus ExtAudioFileGetProperty(ExtAudioFileRef inExtAudioFile, ExtAudioFilePropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

## Return Value

A result code.

## Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inExtAudioFile`: The extended audio file object to get a property value from.
- `inPropertyID`: The property whose value you want.
- `ioPropertyDataSize`: On input, the size of the memory pointed to by the `outPropertyData` parameter. On output, the size of the property value.
- `outPropertyData`: On output, the property value you wanted to get.

## See Also

### Configuring Properties for Extended Audio File Objects
- [func ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./extaudiofilegetpropertyinfo%28_,_,_,_%29.md)
  Gets information about an extended audio file object property.
- [func ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./extaudiofilesetproperty%28_,_,_,_%29.md)
  Sets a property value for an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilegetproperty(_:_:_:_:))*