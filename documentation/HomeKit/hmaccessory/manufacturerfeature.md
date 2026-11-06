# HMAccessory.ManufacturerFeature

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

A manufacturer-declared extension feature for an accessory.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
struct ManufacturerFeature
```

## Topics

### Initializers
- [init(name: String, id: String?, kind: HMAccessory.ManufacturerFeature.Kind)](./manufacturerfeature/init%28name,id,kind%29.md)
  Creates a manufacturer-declared extension feature.
### Instance Properties
- [let id: String?](./manufacturerfeature/id.md)
  The identifier for the feature.
- [let kind: HMAccessory.ManufacturerFeature.Kind](./manufacturerfeature/kind-swift.property.md)
  The category of the feature.
- [let name: String](./manufacturerfeature/name.md)
  The localized display name for the feature.
### Enumerations
- [HMAccessory.ManufacturerFeature.Kind](./manufacturerfeature/kind-swift.enum.md)
  The category of a manufacturer-declared extension feature.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing manufacturer feature extensions
- [var manufacturerFeatures: [HMAccessory.ManufacturerFeature]](./manufacturerfeatures.md)
  The list of manufacturer-declared extension features available for this accessory.
- [func showManufacturerExtension(for: HMAccessory.ManufacturerFeature.Kind, featureID: String?) async throws](./showmanufacturerextension%28for,featureid%29.md)
  Presents the user interface for a manufacturer feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeature)*