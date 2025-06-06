# Basic Behaviors

**Framework**: Swift

Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.

## Topics

### Equality and Ordering
- [protocol Equatable](equatable.md)
  A type that can be compared for value equality.
- [protocol Comparable](comparable.md)
  A type that can be compared using the relational operators `<`, `<=`, `>=`, and `>`.
- [protocol Identifiable](identifiable.md)
  A class of types whose instances hold the value of an entity with stable identity.
### Copying
- [protocol Copyable](copyable.md)
  A type whose values can be implicitly or explicitly copied.
- [protocol BitwiseCopyable](bitwisecopyable.md)
### Sets and Dictionaries
- [protocol Hashable](hashable.md)
  A type that can be hashed into a `Hasher` to produce an integer hash value.
- [struct Hasher](hasher.md)
  The universal hash function used by `Set` and `Dictionary`.
### String Representation
- [protocol CustomStringConvertible](customstringconvertible.md)
  A type with a customized textual representation.
- [protocol LosslessStringConvertible](losslessstringconvertible.md)
  A type that can be represented as a string in a lossless, unambiguous way.
- [protocol CustomDebugStringConvertible](customdebugstringconvertible.md)
  A type with a customized textual representation suitable for debugging purposes.
### Raw Representation
- [protocol CaseIterable](caseiterable.md)
  A type that provides a collection of all of its values.
- [protocol RawRepresentable](rawrepresentable.md)
  A type that can be converted to and from an associated raw value.

## See Also

- [Encoding, Decoding, and Serialization](encoding-decoding-and-serialization.md)
  Serialize and deserialize instances of your types with implicit or customized encoding.
- [Initialization with Literals](initialization-with-literals.md)
  Allow values of your type to be expressed using different kinds of literals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/basic-behaviors)*