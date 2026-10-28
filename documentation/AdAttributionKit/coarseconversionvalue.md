# CoarseConversionValue

**Framework**: AdAttributionKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe developer-defined, relative-attribution conversion values.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CoarseConversionValue
```

## Overview

Use these values to differentiate between the value of a person’s actions that are meaningful for a specific interaction. These values have no effect on the framework, but calling the [`updateConversionValue(_:lockPostback:)`](./postback/updateconversionvalue%28_,lockpostback%29.md) method with the value with [`CoarseConversionValue.low`](./coarseconversionvalue/low.md), for example, causes the postback that the ad network receives to have a field `"coarse-conversion-value": "low"`.

## Topics

### Enumeration Cases
- [CoarseConversionValue.high](./coarseconversionvalue/high.md)
  A value that represents a developer-defined, coarse conversion value that is high.
- [CoarseConversionValue.low](./coarseconversionvalue/low.md)
  A value that represents a developer-defined, coarse conversion value that is low.
- [CoarseConversionValue.medium](./coarseconversionvalue/medium.md)
  A value that represents a developer-defined, coarse conversion value that is medium.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Postbacks
- [struct Postback](./postback.md)
  A structure that provides methods you use to update conversion values for ad attributions.
- [struct PostbackUpdate](./postbackupdate.md)
  Values you use to update properties in a postback, such as the conversion value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/coarseconversionvalue)*