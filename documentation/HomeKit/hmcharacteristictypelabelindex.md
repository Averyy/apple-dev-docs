# HMCharacteristicTypeLabelIndex

**Framework**: HomeKit  
**Kind**: var

The index of the label for the service on an accessory with multiple instances of the same service.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
let HMCharacteristicTypeLabelIndex: String
```

#### Discussion

The corresponding value is an integer that’s greater than or equal to `1`. When the value for the label namespace characteristic is [`HMCharacteristicValueLabelNamespace.dot`](hmcharacteristicvaluelabelnamespace/dot.md), the label index indicates the number of dots, like `.`, `..`, `...`, and so on. When the value for the label namespace characteristic is [`HMCharacteristicValueLabelNamespace.numeral`](hmcharacteristicvaluelabelnamespace/numeral.md), the label index indicates the arabic numeral, like `1`, `2`, `3`, and so on.

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

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypelabelindex)*