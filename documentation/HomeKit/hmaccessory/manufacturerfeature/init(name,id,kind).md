# init(name:id:kind:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a manufacturer-declared extension feature.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
init(name: String, id: String?, kind: HMAccessory.ManufacturerFeature.Kind)
```

## Discussion

Don’t call this initializer directly.

Access the instances of this type in the [`manufacturerFeatures`](../manufacturerfeatures.md) property. To display a feature, call [`showManufacturerExtension(for:featureID:)`](../showmanufacturerextension%28for,featureid%29.md) with that feature’s identifier and kind.

## Parameters

- `name`: The localized display name for the content.
- `id`: The content identifier.
- `kind`: The category of content being presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeature/init(name:id:kind:))*