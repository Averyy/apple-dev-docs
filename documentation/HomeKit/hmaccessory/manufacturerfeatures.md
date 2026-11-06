# manufacturerFeatures

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The list of manufacturer-declared extension features available for this accessory.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
var manufacturerFeatures: [HMAccessory.ManufacturerFeature] { get async throws }
```

## Discussion

If the accessory has no installed manufacturer extension and no fallback content, this property’s value is an empty array.

Trying to access this property when the accessory is not yet associated with a home throws an error.

## See Also

### Accessing manufacturer feature extensions
- [func showManufacturerExtension(for: HMAccessory.ManufacturerFeature.Kind, featureID: String?) async throws](./showmanufacturerextension%28for,featureid%29.md)
  Presents the user interface for a manufacturer feature.
- [HMAccessory.ManufacturerFeature](./manufacturerfeature.md)
  A manufacturer-declared extension feature for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/manufacturerfeatures)*