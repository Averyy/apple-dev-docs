# AtomicOptionalRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [UnsafeRawPointer.AtomicOptionalRepresentation](unsaferawpointer/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming UnsafeRawPointer.AtomicOptionalRepresentation) -> UnsafeRawPointer?](unsaferawpointer/decodeatomicoptionalrepresentation(_:).md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func encodeAtomicOptionalRepresentation(consuming UnsafeRawPointer?) -> UnsafeRawPointer.AtomicOptionalRepresentation](unsaferawpointer/encodeatomicoptionalrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/atomicoptionalrepresentable-implementations)*