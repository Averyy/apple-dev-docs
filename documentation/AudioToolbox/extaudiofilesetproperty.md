# ExtAudioFileSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets a property value for an extended audio file object.

**Availability**:
- iOS 2.1+
- iPadOS 2.1+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ExtAudioFileSetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object to set a property value on.
- `inPropertyID`: The property whose value you want to set.
- `inPropertyDataSize`: The size of the property value, in bytes.
- `inPropertyData`: The value you want to apply to the specified property.

## See Also

- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](extaudiofilegetproperty(_:_:_:_:).md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](extaudiofilegetpropertyinfo(_:_:_:_:).md)
  Gets information about an extended audio file object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilesetproperty(_:_:_:_:))*