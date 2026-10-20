# AtomicOptionalRepresentable

**Framework**: Synchronization  
**Kind**: protocol  
**Role**: Protocol

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
- [associatedtype AtomicOptionalRepresentation : BitwiseCopyable](./atomicoptionalrepresentable/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming Self.AtomicOptionalRepresentation) -> Self?](./atomicoptionalrepresentable/decodeatomicoptionalrepresentation%28_%29.md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func encodeAtomicOptionalRepresentation(consuming Self?) -> Self.AtomicOptionalRepresentation](./atomicoptionalrepresentable/encodeatomicoptionalrepresentation%28_%29.md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.

## Relationships

### Inherits From
- [AtomicRepresentable](./atomicrepresentable.md)
### Conforming Types
- [ObjectIdentifier](../Swift/objectidentifier.md)
- [OpaquePointer](../Swift/opaquepointer.md)
- [Unmanaged](../Swift/unmanaged.md)
- [UnsafeMutablePointer](../Swift/unsafemutablepointer.md)
- [UnsafeMutableRawPointer](../Swift/unsafemutablerawpointer.md)
- [UnsafePointer](../Swift/unsafepointer.md)
- [UnsafeRawPointer](../Swift/unsaferawpointer.md)

## See Also

### Atomic Values
- [struct Atomic](./atomic.md)
  An atomic value.
- [struct AtomicLazyReference](./atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [struct WordPair](./wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicRepresentable](./atomicrepresentable.md)
  A type that supports atomic operations through a separate atomic storage representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable)*