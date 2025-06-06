# AtomicRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [UnsafePointer.AtomicRepresentation](unsafepointer/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming UnsafePointer<Pointee>.AtomicRepresentation) -> UnsafePointer<Pointee>](unsafepointer/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(consuming UnsafePointer<Pointee>) -> UnsafePointer<Pointee>.AtomicRepresentation](unsafepointer/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafepointer/atomicrepresentable-implementations)*