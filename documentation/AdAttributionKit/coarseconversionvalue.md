# CoarseConversionValue

**Framework**: AdAttributionKit  
**Kind**: enum

Values that describe developer-defined, relative-attribution conversion values.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
enum CoarseConversionValue
```

#### Overview

Use these values to differentiate between the value of a person’s actions that are meaningful for a specific interaction. These values have no effect on the framework, but calling the [`updateConversionValue(_:lockPostback:)`](postback/updateconversionvalue(_:lockpostback:).md) method with the value with [`CoarseConversionValue.low`](coarseconversionvalue/low.md), for example, causes the postback that the ad network receives to have a field `"coarse-conversion-value": "low"`.

## Topics

### Enumeration Cases
- [CoarseConversionValue.high](coarseconversionvalue/high.md)
  A value that represents a developer-defined, coarse conversion value that is high.
- [CoarseConversionValue.low](coarseconversionvalue/low.md)
  A value that represents a developer-defined, coarse conversion value that is low.
- [CoarseConversionValue.medium](coarseconversionvalue/medium.md)
  A value that represents a developer-defined, coarse conversion value that is medium.
### Initializers
- [init?(rawValue: String)](coarseconversionvalue/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](coarseconversionvalue/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [CoarseConversionValue.RawValue](coarseconversionvalue/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](coarseconversionvalue/equatable-implementations.md)
- [RawRepresentable Implementations](coarseconversionvalue/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Postback](postback.md)
  A structure that provides methods you use to update conversion values for ad attributions.
- [struct PostbackUpdate](postbackupdate.md)
  Values you use to update properties in a postback, such as the conversion value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/coarseconversionvalue)*