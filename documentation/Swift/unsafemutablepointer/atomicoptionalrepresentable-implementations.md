# AtomicOptionalRepresentable Implementations

**Framework**: Swift

## Topics

### Type Aliases
- [UnsafeMutablePointer.AtomicOptionalRepresentation](unsafemutablepointer/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming UnsafeMutablePointer<Pointee>.AtomicOptionalRepresentation) -> UnsafeMutablePointer<Pointee>?](unsafemutablepointer/decodeatomicoptionalrepresentation(_:).md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func encodeAtomicOptionalRepresentation(consuming UnsafeMutablePointer<Pointee>?) -> UnsafeMutablePointer<Pointee>.AtomicOptionalRepresentation](unsafemutablepointer/encodeatomicoptionalrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/atomicoptionalrepresentable-implementations)*