# showManufacturerExtension(for:featureID:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Presents the user interface for a manufacturer feature.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
func showManufacturerExtension(for kind: HMAccessory.ManufacturerFeature.Kind, featureID: String? = nil) async throws
```

## Parameters

- `kind`: The kind of feature to present.
- `featureID`: Provide an identifier from one of the features in the [`manufacturerFeatures`](./manufacturerfeatures.md) property, or pass `nil` if `kind` is [`HMAccessory.ManufacturerFeature.Kind.troubleshooting`](./manufacturerfeature/kind-swift.enum/troubleshooting.md) or [`HMAccessory.ManufacturerFeature.Kind.productManual`](./manufacturerfeature/kind-swift.enum/productmanual.md).

## See Also

### Accessing manufacturer feature extensions
- [var manufacturerFeatures: [HMAccessory.ManufacturerFeature]](./manufacturerfeatures.md)
  The list of manufacturer-declared extension features available for this accessory.
- [HMAccessory.ManufacturerFeature](./manufacturerfeature.md)
  A manufacturer-declared extension feature for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/showmanufacturerextension(for:featureid:))*