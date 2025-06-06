# HMCharacteristicTypeIdentify

**Framework**: HomeKit  
**Kind**: var

A control you can use to ask the accessory to identify itself.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeIdentify: String
```

#### Discussion

Use the corresponding write-only Boolean value to ask the accessory to identify itself in the physical world. The identification mechanism, if supported, is specific to the accessory. For example, a light bulb might change state briefly, flashing on or off, to indicate that it has received this command.

## See Also

- [let HMCharacteristicTypeName: String](hmcharacteristictypename.md)
  The name of the accessory.
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
- [let HMCharacteristicTypeActiveIdentifier: String](hmcharacteristictypeactiveidentifier.md)
  An index that maps to the current active Input Source service.
- [let HMCharacteristicTypeIdentifier: String](hmcharacteristictypeidentifier.md)
  The identifier for an accessory.
- [let HMCharacteristicTypeInputDeviceType: String](hmcharacteristictypeinputdevicetype.md)
  The accessory input device type.
- [let HMCharacteristicTypeInputSourceType: String](hmcharacteristictypeinputsourcetype.md)
  The accessory input source type.
- [let HMCharacteristicTypeConfiguredName: String](hmcharacteristictypeconfiguredname.md)
  A `UTF‑8` encoded user visible name on an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeidentify)*