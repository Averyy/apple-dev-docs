# showManufacturerExtension(for:featureID:)

**Framework**: HomeKit  
**Kind**: method

Presents the system-rendered UI for one manufacturer feature.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
func showManufacturerExtension(for kind: HMAccessory.ManufacturerFeature.Kind, featureID: String? = nil) async throws
```

#### Discussion

Returns once the request has been handed off to the system; throws on any error encountered while attempting to launch.

## Parameters

- `kind`: Selects the kind of feature to present.
- `featureID`: The catalog identifier returned in the matching [`HMAccessory.ManufacturerFeature`](hmaccessory/manufacturerfeature.md) (and `nil` for `.troubleshooting` and `.productManual`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/showmanufacturerextension(for:featureid:))*