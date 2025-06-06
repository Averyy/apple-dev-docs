# ExtAudioFileGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object to get property information from.
- `inPropertyID`: The property you want information about.
- `outSize`: On output, the size of the property value in bytes. Can be   on output.
- `outWritable`: On output, a Boolean value indicating whether the property value is writable (  means writable). Can be   on output.

## See Also

- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](extaudiofilegetproperty(_:_:_:_:).md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus](extaudiofilesetproperty(_:_:_:_:).md)
  Sets a property value for an extended audio file object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilegetpropertyinfo(_:_:_:_:))*