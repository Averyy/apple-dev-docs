# FinanceStore.UpdateFrequency

**Framework**: FinanceKit  
**Kind**: enum

The frequencies that apps can register for updates with.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum UpdateFrequency
```

#### Overview

These represent the expected interval that can occur between updates delivered to background delivery registrations.

## Topics

### Operators
- [static func == (FinanceStore.UpdateFrequency, FinanceStore.UpdateFrequency) -> Bool](financestore/updatefrequency/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FinanceStore.UpdateFrequency.daily](financestore/updatefrequency/daily.md)
  Get notified within a day of data updating.
- [FinanceStore.UpdateFrequency.hourly](financestore/updatefrequency/hourly.md)
  Get notified within an hour of data updating.
- [FinanceStore.UpdateFrequency.weekly](financestore/updatefrequency/weekly.md)
  Get notified within a week of data updating.
### Initializers
- [init(from: any Decoder) throws](financestore/updatefrequency/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](financestore/updatefrequency/hashvalue.md)
  The hash value.
- [var interval: TimeInterval](financestore/updatefrequency/interval.md)
### Instance Methods
- [func encode(to: any Encoder) throws](financestore/updatefrequency/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](financestore/updatefrequency/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](financestore/updatefrequency/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/updatefrequency)*