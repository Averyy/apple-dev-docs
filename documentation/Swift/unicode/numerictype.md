# Unicode.NumericType

**Framework**: Swift  
**Kind**: enum

The numeric type of a scalar.

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
enum NumericType
```

#### Overview

Scalars with a non-nil numeric type include numbers, fractions, numeric superscripts and subscripts, and circled or otherwise decorated number glyphs.

Some letterlike scalars used in numeric systems, such as Greek or Latin letters, do not have a non-nil numeric type, in order to prevent programs from incorrectly interpreting them as numbers in non-numeric contexts.

## Topics

### Operators
- [static func == (Unicode.NumericType, Unicode.NumericType) -> Bool](unicode/numerictype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Unicode.NumericType.decimal](unicode/numerictype/decimal.md)
  A digit that is commonly understood to form base-10 numbers.
- [Unicode.NumericType.digit](unicode/numerictype/digit.md)
  A digit that does not meet the requirements of the `decimal` numeric type.
- [Unicode.NumericType.numeric](unicode/numerictype/numeric.md)
  A digit that does not meet the requirements of the `decimal` numeric type or a non-digit numeric value.
### Instance Properties
- [var hashValue: Int](unicode/numerictype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](unicode/numerictype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](unicode/numerictype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [Unicode.GeneralCategory](unicode/generalcategory.md)
  The most general classification of a Unicode scalar.
- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)
  The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/numerictype)*