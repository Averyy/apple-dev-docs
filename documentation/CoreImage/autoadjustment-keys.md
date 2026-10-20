# Autoadjustment Keys

**Framework**: Core Image  
**Role**: API Collection

Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](./ciimage/autoadjustmentfilters%28options%29.md) method.

## Topics

### Constants
- [static let enhance: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let redEye: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/redeye.md)
  A key used to specify whether to return a red eye filter.
- [static let features: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let crop: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/crop.md)
  A key used to specify whether to return a filter that crops the image to focus on detected features.
- [static let level: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.

## See Also

### Getting Autoadjustment Filters
- [func autoAdjustmentFilters() -> [CIFilter]](./ciimage/autoadjustmentfilters%28%29.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]?) -> [CIFilter]](./ciimage/autoadjustmentfilters%28options%29.md)
  Returns a subset of automatically selected and configured filters for adjusting the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/autoadjustment-keys)*