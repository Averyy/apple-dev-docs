# AtomicOptionalRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [Unmanaged.AtomicOptionalRepresentation](unmanaged/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming Unmanaged<Instance>.AtomicOptionalRepresentation) -> Unmanaged<Instance>?](unmanaged/decodeatomicoptionalrepresentation(_:).md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func encodeAtomicOptionalRepresentation(consuming Unmanaged<Instance>?) -> Unmanaged<Instance>.AtomicOptionalRepresentation](unmanaged/encodeatomicoptionalrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged/atomicoptionalrepresentable-implementations)*