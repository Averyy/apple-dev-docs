# Managed Buffers

**Framework**: Swift

Build your own buffer-backed collection types.

## Topics

### Buffer Implementation
- [class ManagedBuffer](managedbuffer.md)
  A class whose instances contain a property of type `Header` and raw storage for an array of `Element`, whose size is determined at instance creation.
- [struct ManagedBufferPointer](managedbufferpointer.md)
  Contains a buffer object, and provides access to an instance of `Header` and contiguous storage for an arbitrary number of `Element` instances stored in that buffer.
### Uniqueness Checking
- [func isKnownUniquelyReferenced<T>(inout T?) -> Bool](isknownuniquelyreferenced(_:)-98zpp.md)
  Returns a Boolean value indicating whether the given object is known to have a single strong reference.
- [func isKnownUniquelyReferenced<T>(inout T) -> Bool](isknownuniquelyreferenced(_:)-5kvtu.md)
  Returns a Boolean value indicating whether the given object is known to have a single strong reference.

## See Also

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md)
  Write generic code that works with any collection, or build your own collection types.
- [Supporting Types](supporting-types.md)
  Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managed-buffers)*