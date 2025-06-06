# AudioServicesSetProperty(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value for a specified System Sound Services property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesSetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

System Sound Services properties are listed and described in [`System Sound Services Property Identifiers`](1405268-system-sound-services-property-i.md).

## Parameters

- `inPropertyID`: The property whose value you want to set.
- `inSpecifierSize`: The size of the buffer pointed to by the   parameter. Pass   if no specifier buffer is required.
- `inSpecifier`: A pointer to a specifier buffer, if such a buffer is required by the property about which you want information. Pass   if no specifier is required.
- `inPropertyDataSize`: The size, in bytes, of the buffer pointed to by the   parameter.
- `inPropertyData`: The property value you want to set.

## See Also

- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioservicesgetpropertyinfo(_:_:_:_:_:).md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audioservicesgetproperty(_:_:_:_:_:).md)
  Gets a specified System Sound Services property value.
- [typealias AudioServicesPropertyID](audioservicespropertyid.md)
  The data type for a system sound property identifier.
- [System Sound Services Property Identifiers](1405268-system-sound-services-property-i.md)
  Property identifiers used when playing alerts with System Sound Services.
- [Audio Hardware Services Properties](1405208-audio-hardware-services-properti.md)
  Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicessetproperty(_:_:_:_:_:))*