# HMAccessory.ManufacturerFeature

**Framework**: HomeKit  
**Kind**: struct

A manufacturer-declared extension feature available for an accessory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct ManufacturerFeature
```

#### Overview

`name` carries the localized display name. `id` is optional because `.troubleshooting` and `.productManual` features carry no per-feature identifier. `kind` distinguishes the five feature categories the system understands.

## Topics

### Initializers
- [init(name: String, id: String?, kind: HMAccessory.ManufacturerFeature.Kind)](hmaccessory/manufacturerfeature/init(name:id:kind:).md)
### Instance Properties
- [let id: String?](hmaccessory/manufacturerfeature/id.md)
- [let kind: HMAccessory.ManufacturerFeature.Kind](hmaccessory/manufacturerfeature/kind-swift.property.md)
- [let name: String](hmaccessory/manufacturerfeature/name.md)
### Enumerations
- [HMAccessory.ManufacturerFeature.Kind](hmaccessory/manufacturerfeature/kind-swift.enum.md)
  The category of a manufacturer-declared extension feature.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeature)*