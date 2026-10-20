# ExtAudioFileGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets information about an extended audio file object property.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

```c
extern OSStatus ExtAudioFileGetPropertyInfo(ExtAudioFileRef inExtAudioFile, ExtAudioFilePropertyID inPropertyID, UInt32 *outSize, Boolean *outWritable);
```

#### Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object to get property information from.
- `inPropertyID`: The property you want information about.
- `outSize`: On output, the size of the property value in bytes. Can be `NULL` on output.
- `outWritable`: On output, a Boolean value indicating whether the property value is writable (`true` means writable). Can be `NULL` on output.

## See Also

### Configuring Properties for Extended Audio File Objects
- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./extaudiofilegetproperty%28_,_,_,_%29.md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./extaudiofilesetproperty%28_,_,_,_%29.md)
  Sets a property value for an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilegetpropertyinfo(_:_:_:_:))*