# AtomicOptionalRepresentable

**Framework**: Synchronization  
**Kind**: protocol

An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol AtomicOptionalRepresentable : AtomicRepresentable
```

## Topics

### Associated Types
- [associatedtype AtomicOptionalRepresentation : BitwiseCopyable](atomicoptionalrepresentable/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming Self.AtomicOptionalRepresentation) -> Self?](atomicoptionalrepresentable/decodeatomicoptionalrepresentation(_:).md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func encodeAtomicOptionalRepresentation(consuming Self?) -> Self.AtomicOptionalRepresentation](atomicoptionalrepresentable/encodeatomicoptionalrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.

## Relationships

### Inherits From
- [AtomicRepresentable](atomicrepresentable.md)
### Conforming Types
- [ObjectIdentifier](../swift/objectidentifier.md)
- [OpaquePointer](../swift/opaquepointer.md)
- [Unmanaged](../swift/unmanaged.md)
- [UnsafeMutablePointer](../swift/unsafemutablepointer.md)
- [UnsafeMutableRawPointer](../swift/unsafemutablerawpointer.md)
- [UnsafePointer](../swift/unsafepointer.md)
- [UnsafeRawPointer](../swift/unsaferawpointer.md)

## See Also

- [struct Atomic](atomic.md)
  An atomic value.
- [struct AtomicLazyReference](atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [struct WordPair](wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicRepresentable](atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable)*