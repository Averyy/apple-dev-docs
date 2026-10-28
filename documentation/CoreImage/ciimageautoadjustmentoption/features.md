# features

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A key used to specify an array of features that you want to apply enhancement and red eye filters to.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let features: CIImageAutoAdjustmentOption
```

```c
extern CIImageAutoAdjustmentOption const kCIImageAutoAdjustFeatures;
```

## Discussion

The associated value is an array of `CIFeature` objects. If you don’t supply an array, the Core Image searches for features using the `CIDetector` class.

## See Also

### Type Properties
- [static let crop: CIImageAutoAdjustmentOption](./crop.md)
  A key used to specify whether to return a filter that crops the image to focus on detected features.
- [static let enhance: CIImageAutoAdjustmentOption](./enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let level: CIImageAutoAdjustmentOption](./level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [static let redEye: CIImageAutoAdjustmentOption](./redeye.md)
  A key used to specify whether to return a red eye filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/features)*