# HMCharacteristicTypeActiveIdentifier

**Framework**: HomeKit  
**Kind**: var

An index that maps to the current active Input Source service.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let HMCharacteristicTypeActiveIdentifier: String
```

#### Discussion

This characteristic describes the current input source of a television by referencing the [`HMServiceTypeInputSource`](hmservicetypeinputsource.md). The Active Identifier characteristic’s value should be a valid value within the identifiers of the Input Source service instances linked to the television service. The value of the characteristic is a `UInt32` integer.

## See Also

- [let HMCharacteristicTypeName: String](hmcharacteristictypename.md)
  The name of the accessory.
- [let HMCharacteristicTypeIdentify: String](hmcharacteristictypeidentify.md)
  A control you can use to ask the accessory to identify itself.
- [let HMCharacteristicTypeVersion: String](hmcharacteristictypeversion.md)
  The version of the accessory.
- [let HMCharacteristicTypeLogs: String](hmcharacteristictypelogs.md)
  Log data for the accessory.
- [let HMCharacteristicTypeAdminOnlyAccess: String](hmcharacteristictypeadminonlyaccess.md)
  An indicator of whether the accessory accepts only administrator access.
- [let HMCharacteristicTypeHardwareVersion: String](hmcharacteristictypehardwareversion.md)
  The hardware version of the accessory.
- [let HMCharacteristicTypeSoftwareVersion: String](hmcharacteristictypesoftwareversion.md)
  The software version of the accessory.
- [let HMCharacteristicTypeLabelIndex: String](hmcharacteristictypelabelindex.md)
  The index of the label for the service on an accessory with multiple instances of the same service.
- [let HMCharacteristicTypeLabelNamespace: String](hmcharacteristictypelabelnamespace.md)
  The naming schema used to label the services on an accessory with multiple services of the same type.
- [let HMCharacteristicTypeIdentifier: String](hmcharacteristictypeidentifier.md)
  The identifier for an accessory.
- [let HMCharacteristicTypeInputDeviceType: String](hmcharacteristictypeinputdevicetype.md)
  The accessory input device type.
- [let HMCharacteristicTypeInputSourceType: String](hmcharacteristictypeinputsourcetype.md)
  The accessory input source type.
- [let HMCharacteristicTypeConfiguredName: String](hmcharacteristictypeconfiguredname.md)
  A `UTF‑8` encoded user visible name on an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeactiveidentifier)*