# CIImageAutoAdjustmentOption

**Framework**: Core Image  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct CIImageAutoAdjustmentOption
```

```c
typedef NSString * CIImageAutoAdjustmentOption;
```

## Topics

### Initializers
- [init(rawValue: String)](./ciimageautoadjustmentoption/init%28rawvalue%29.md)
### Type Properties
- [static let crop: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/crop.md)
  A key used to specify whether to return a filter that crops the image to focus on detected features.
- [static let enhance: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/enhance.md)
  A key used to specify whether to return enhancement filters.
- [static let features: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/features.md)
  A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [static let level: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/level.md)
  A key used to specify whether to return a filter that rotates the image to keep a level perspective.
- [static let redEye: CIImageAutoAdjustmentOption](./ciimageautoadjustmentoption/redeye.md)
  A key used to specify whether to return a red eye filter.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption)*