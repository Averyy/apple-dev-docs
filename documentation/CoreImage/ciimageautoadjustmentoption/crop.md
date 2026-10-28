# crop

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A key used to specify whether to return a filter that crops the image to focus on detected features.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let crop: CIImageAutoAdjustmentOption
```

```c
extern CIImageAutoAdjustmentOption const kCIImageAutoAdjustCrop;
```

## Discussion

The value associated with this key is a `CFBoolean` value. If `true`, the returned filters include an operation that crops the image around the features specified with the [`features`](./features.md) option (or any features detected in the image, if that option is not present). Supply `false` to indicate not to return a crop filter. If you don’t specify this option, Core Image assumes its value is `false`.

## See Also

### Type Properties
- [static let enhance: CIImageAutoAdjustmentOption](./enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let features: CIImageAutoAdjustmentOption](./features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let level: CIImageAutoAdjustmentOption](./level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [static let redEye: CIImageAutoAdjustmentOption](./redeye.md)
  A key used to specify whether to return a red eye filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/crop)*