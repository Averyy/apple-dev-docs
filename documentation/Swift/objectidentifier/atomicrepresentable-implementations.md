# AtomicRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [ObjectIdentifier.AtomicRepresentation](objectidentifier/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming ObjectIdentifier.AtomicRepresentation) -> ObjectIdentifier](objectidentifier/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(consuming ObjectIdentifier) -> ObjectIdentifier.AtomicRepresentation](objectidentifier/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/objectidentifier/atomicrepresentable-implementations)*