# ElectricityGuidance.Options

**Framework**: EnergyKit  
**Kind**: enum

An enumeration that describes additional factors that influence the weight of a value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
enum Options
```

#### Overview

A person’s utility rate plan is an example of an additional factor that influences the weight of a value.

## Topics

### Getting the options
- [ElectricityGuidance.Options.locationHasRatePlan](electricityguidance/options-swift.enum/locationhasrateplan.md)
  Indicates whether the energy venue where the guidance was generated has rate plan information available.
- [ElectricityGuidance.Options.guidanceIncorporatesRatePlan](electricityguidance/options-swift.enum/guidanceincorporatesrateplan.md)
  Indicates whether the electricity guidance incorporated rate plan information.
### Decoding
- [init(from: any Decoder) throws](electricityguidance/options-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (ElectricityGuidance.Options, ElectricityGuidance.Options) -> Bool](electricityguidance/options-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](electricityguidance/options-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](electricityguidance/options-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](electricityguidance/options-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [ElectricityGuidance.Options.AllCases](electricityguidance/options-swift.enum/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [ElectricityGuidance.Options]](electricityguidance/options-swift.enum/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](electricityguidance/options-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ElectricityGuidance.Value](electricityguidance/value.md)
  A normalized weighting value associated with a period of time, describing when to shift or reduce electricity use.
- [let values: [ElectricityGuidance.Value]](electricityguidance/values.md)
  A series of weighted values for intervals of time, describing when to shift or reduce electricity use.
- [let options: Set<ElectricityGuidance.Options>](electricityguidance/options-swift.property.md)
  The additional factors that influence the weight of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/options-swift.enum)*