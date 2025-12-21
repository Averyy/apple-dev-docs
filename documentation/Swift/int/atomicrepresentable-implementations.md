# AtomicRepresentable Implementations

**Framework**: Swift

## Topics

### Type Methods
- [static func decodeAtomicRepresentation(consuming Int.AtomicRepresentation) -> Int](int/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(borrowing Int) -> Int.AtomicRepresentation](int/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/atomicrepresentable-implementations)*