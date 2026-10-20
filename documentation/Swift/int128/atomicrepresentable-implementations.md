# AtomicRepresentable Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Type Aliases
- [typealias AtomicRepresentation](./atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming Int128.AtomicRepresentation) -> Int128](./decodeatomicrepresentation%28_%29.md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(borrowing Int128) -> Int128.AtomicRepresentation](./encodeatomicrepresentation%28_%29.md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/atomicrepresentable-implementations)*