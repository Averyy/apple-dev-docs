# FloatingPointRoundingRule

**Framework**: Swift  
**Kind**: enum

A rule for rounding a floating-point number.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum FloatingPointRoundingRule
```

## Topics

### Operators
- [static func == (FloatingPointRoundingRule, FloatingPointRoundingRule) -> Bool](floatingpointroundingrule/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FloatingPointRoundingRule.awayFromZero](floatingpointroundingrule/awayfromzero.md)
  Round to the closest allowed value whose magnitude is greater than or equal to that of the source.
- [FloatingPointRoundingRule.down](floatingpointroundingrule/down.md)
  Round to the closest allowed value that is less than or equal to the source.
- [FloatingPointRoundingRule.toNearestOrAwayFromZero](floatingpointroundingrule/tonearestorawayfromzero.md)
  Round to the closest allowed value; if two values are equally close, the one with greater magnitude is chosen.
- [FloatingPointRoundingRule.toNearestOrEven](floatingpointroundingrule/tonearestoreven.md)
  Round to the closest allowed value; if two values are equally close, the even one is chosen.
- [FloatingPointRoundingRule.towardZero](floatingpointroundingrule/towardzero.md)
  Round to the closest allowed value whose magnitude is less than or equal to that of the source.
- [FloatingPointRoundingRule.up](floatingpointroundingrule/up.md)
  Round to the closest allowed value that is greater than or equal to the source.
### Instance Properties
- [var hashValue: Int](floatingpointroundingrule/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](floatingpointroundingrule/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](floatingpointroundingrule/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [enum FloatingPointClassification](floatingpointclassification.md)
  The IEEE 754 floating-point classes.
- [enum FloatingPointSign](floatingpointsign.md)
  The sign of a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpointroundingrule)*