# AudioServicesPropertyID

**Framework**: Audio Toolbox  
**Kind**: typealias

The data type for a system sound property identifier.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioServicesPropertyID = UInt32
```

#### Discussion

System Audio Services properties are listed in [`System Sound Services Property Identifiers`](1405268-system-sound-services-property-i.md).

## See Also

- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioservicesgetpropertyinfo(_:_:_:_:_:).md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audioservicesgetproperty(_:_:_:_:_:).md)
  Gets a specified System Sound Services property value.
- [func AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](audioservicessetproperty(_:_:_:_:_:).md)
  Sets the value for a specified System Sound Services property.
- [System Sound Services Property Identifiers](1405268-system-sound-services-property-i.md)
  Property identifiers used when playing alerts with System Sound Services.
- [Audio Hardware Services Properties](1405208-audio-hardware-services-properti.md)
  Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicespropertyid)*