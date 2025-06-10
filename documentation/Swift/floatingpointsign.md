# FloatingPointSign

**Framework**: Swift  
**Kind**: enum

The sign of a floating-point value.

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
@frozen
enum FloatingPointSign
```

## Topics

### Operators
- [static func == (FloatingPointSign, FloatingPointSign) -> Bool](floatingpointsign/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FloatingPointSign.minus](floatingpointsign/minus.md)
  The sign for a negative value.
- [FloatingPointSign.plus](floatingpointsign/plus.md)
  The sign for a positive value.
### Initializers
- [init?(rawValue: Int)](floatingpointsign/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var hashValue: Int](floatingpointsign/hashvalue.md)
  The hash value.
- [var rawValue: Int](floatingpointsign/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Instance Methods
- [func hash(into: inout Hasher)](floatingpointsign/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [FloatingPointSign.RawValue](floatingpointsign/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](floatingpointsign/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [RawRepresentable](rawrepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [enum FloatingPointClassification](floatingpointclassification.md)
  The IEEE 754 floating-point classes.
- [enum FloatingPointRoundingRule](floatingpointroundingrule.md)
  A rule for rounding a floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpointsign)*