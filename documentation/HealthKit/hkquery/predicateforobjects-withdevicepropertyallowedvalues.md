# predicateForObjects(withDeviceProperty:allowedValues:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches all objects created by devices with the specified properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForObjects(withDeviceProperty key: String, allowedValues: Set<String>) -> NSPredicate
```

#### Return Value

A predicate that matches all objects created by a device whose specified property matches one of the allowed values.

#### Discussion

Use this convenience method to create a predicate that finds all the objects saved by matching devices. These predicates let you match multiple values for a single property. For example, you can create a single predicate that matches a number of different `manufacturer` values.

The following sample shows how to create a predicate that matches a list of device model names.

## Parameters

- `key`: A string specifying the device’s property. For a list of valid keys, see Valid Device Property Keys.
- `allowedValues`: A set of strings. These strings represent the target property values.

## Topics

### Valid Device Property Keys
- [let HKDevicePropertyKeyName: String](hkdevicepropertykeyname.md)
  The device’s name.
- [let HKDevicePropertyKeyManufacturer: String](hkdevicepropertykeymanufacturer.md)
  The device’s manufacturer.
- [let HKDevicePropertyKeyModel: String](hkdevicepropertykeymodel.md)
  The device’s model.
- [let HKDevicePropertyKeyHardwareVersion: String](hkdevicepropertykeyhardwareversion.md)
  The device’s hardware version.
- [let HKDevicePropertyKeyFirmwareVersion: String](hkdevicepropertykeyfirmwareversion.md)
  The device’s firmware version.
- [let HKDevicePropertyKeySoftwareVersion: String](hkdevicepropertykeysoftwareversion.md)
  The device’s software version.
- [let HKDevicePropertyKeyLocalIdentifier: String](hkdevicepropertykeylocalidentifier.md)
  A unique identifier for the device on the hardware running the app. For more information, see [`localIdentifier`](hkdevice/localidentifier.md).
- [let HKDevicePropertyKeyUDIDeviceIdentifier: String](hkdevicepropertykeyudideviceidentifier.md)
  The device’s UDI Device Identifier.

## See Also

- [class func predicateForObject(with: UUID) -> NSPredicate](hkquery/predicateforobject(with:).md)
  Returns a predicate that matches an object with the specified universally unique identifier (UUID).
- [class func predicateForObjects(with: Set<UUID>) -> NSPredicate](hkquery/predicateforobjects(with:).md)
  Returns a predicate that matches the objects with the specified  universally unique identifiers (UUIDs).
- [class func predicateForObjects(from: HKSource) -> NSPredicate](hkquery/predicateforobjects(from:)-7j3p2.md)
  Returns a predicate that matches all the objects that were created by the provided source.
- [class func predicateForObjects(from: Set<HKSource>) -> NSPredicate](hkquery/predicateforobjects(from:)-89b4t.md)
  Returns a predicate that matches all the objects that were created by any of the provided sources.
- [class func predicateForObjects(from: Set<HKDevice>) -> NSPredicate](hkquery/predicateforobjects(from:)-9h87f.md)
  Returns a predicate that matches all the objects that were created by any of the provided devices.
- [class func predicateForObjects(from: Set<HKSourceRevision>) -> NSPredicate](hkquery/predicateforobjects(from:)-1ar4g.md)
  Returns a predicate that matches all the objects that were created by any of the provided source revisions.
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:).md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:allowedvalues:).md)
  Returns a predicate that matches objects based on the provided metadata key and an array of target values.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:operatortype:value:).md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.
- [class func predicateForObjectsWithNoCorrelation() -> NSPredicate](hkquery/predicateforobjectswithnocorrelation.md)
  Returns a predicate that matches all objects that are not associated with a HealthKit correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjects(withdeviceproperty:allowedvalues:))*