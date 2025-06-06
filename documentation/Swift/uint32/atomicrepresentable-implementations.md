# AtomicRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [typealias AtomicRepresentation](uint32/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming UInt32.AtomicRepresentation) -> UInt32](uint32/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(borrowing UInt32) -> UInt32.AtomicRepresentation](uint32/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/atomicrepresentable-implementations)*