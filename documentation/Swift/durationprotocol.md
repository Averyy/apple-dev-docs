# DurationProtocol

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type that defines a duration for a given `InstantProtocol` type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol DurationProtocol : AdditiveArithmetic, Comparable, Sendable
```

## Topics

### Operators
- [static func * (Self, Int) -> Self](./durationprotocol/star%28_,_%29.md)
- [static func *= (inout Self, Int)](./durationprotocol/stareq%28_,_%29.md)
- [static func / (Self, Self) -> Double](./durationprotocol/op%28_,_%29-4x9r1.md)
- [static func / (Self, Int) -> Self](./durationprotocol/op%28_,_%29-6l82o.md)
- [static func /= (inout Self, Int)](./durationprotocol/opeq%28_,_%29.md)

## Relationships

### Inherits From
- [AdditiveArithmetic](./additivearithmetic.md)
- [Comparable](./comparable.md)
- [Equatable](./equatable.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
### Conforming Types
- [Duration](./duration.md)

## See Also

### Durations
- [struct Duration](./duration.md)
  A representation of high precision time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/durationprotocol)*