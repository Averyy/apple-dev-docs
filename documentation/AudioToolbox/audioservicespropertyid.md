# AudioServicesPropertyID

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

The data type for a system sound property identifier.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioServicesPropertyID = UInt32
```

```c
typedef UInt32 AudioServicesPropertyID;
```

#### Discussion

System Audio Services properties are listed in [System Sound Services Property Identifiers](./api-1405268-system-sound-services-property-i.md).

## See Also

### Managing System Sound Services Properties
- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audioservicesgetpropertyinfo%28_,_,_,_,_%29.md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audioservicesgetproperty%28_,_,_,_,_%29.md)
  Gets a specified System Sound Services property value.
- [func AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](./audioservicessetproperty%28_,_,_,_,_%29.md)
  Sets the value for a specified System Sound Services property.
- [System Sound Services Property Identifiers](./api-1405268-system-sound-services-property-i.md)
  Property identifiers used when playing alerts with System Sound Services.
- [Audio Hardware Services Properties](./api-1405208-audio-hardware-services-properti.md)
  Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicespropertyid)*