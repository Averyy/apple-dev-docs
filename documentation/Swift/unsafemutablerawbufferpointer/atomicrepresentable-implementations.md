# AtomicRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [UnsafeMutableRawBufferPointer.AtomicRepresentation](unsafemutablerawbufferpointer/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming UnsafeMutableRawBufferPointer.AtomicRepresentation) -> UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(consuming UnsafeMutableRawBufferPointer) -> UnsafeMutableRawBufferPointer.AtomicRepresentation](unsafemutablerawbufferpointer/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/atomicrepresentable-implementations)*