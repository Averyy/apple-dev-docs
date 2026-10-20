# HMAccessory.ManufacturerFeature

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

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
- [init(name: String, id: String?, kind: HMAccessory.ManufacturerFeature.Kind)](./manufacturerfeature/init%28name,id,kind%29.md)
### Instance Properties
- [let id: String?](./manufacturerfeature/id.md)
- [let kind: HMAccessory.ManufacturerFeature.Kind](./manufacturerfeature/kind-swift.property.md)
- [let name: String](./manufacturerfeature/name.md)
### Enumerations
- [HMAccessory.ManufacturerFeature.Kind](./manufacturerfeature/kind-swift.enum.md)
  The category of a manufacturer-declared extension feature.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeature)*