# ExtAudioFileSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus ExtAudioFileSetProperty(ExtAudioFileRef inExtAudioFile, ExtAudioFilePropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

## Return Value

A result code.

## Parameters

- `inExtAudioFile`: The extended audio file object to set a property value on.
- `inPropertyID`: The property whose value you want to set.
- `inPropertyDataSize`: The size of the property value, in bytes.
- `inPropertyData`: The value you want to apply to the specified property.

## See Also

### Configuring Properties for Extended Audio File Objects
- [func ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./extaudiofilegetproperty%28_,_,_,_%29.md)
  Gets a property value from an extended audio file object.
- [func ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./extaudiofilegetpropertyinfo%28_,_,_,_%29.md)
  Gets information about an extended audio file object property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilesetproperty(_:_:_:_:))*