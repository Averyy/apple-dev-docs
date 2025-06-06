# AutoreleasingUnsafeMutablePointer

**Framework**: Swift  
**Kind**: struct

A mutable pointer addressing an Objective-C reference that doesn’t own its target.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct AutoreleasingUnsafeMutablePointer<Pointee>
```

## Mentions

- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md)

#### Overview

`Pointee` must be a class type or `Optional<C>` where `C` is a class.

This type has implicit conversions to allow passing any of the following to a C or ObjC API:

- `nil`, which gets passed as a null pointer,
- an inout argument of the referenced type, which gets passed as a pointer to a writeback temporary with autoreleasing ownership semantics,
- an `UnsafeMutablePointer<Pointee>`, which is passed as-is.

Passing pointers to mutable arrays of ObjC class pointers is not directly supported. Unlike `UnsafeMutablePointer<Pointee>`, `AutoreleasingUnsafeMutablePointer<Pointee>` must reference storage that does not own a reference count to the referenced value. UnsafeMutablePointer’s operations, by contrast, assume that the referenced storage owns values loaded from or stored to it.

This type does not carry an owner pointer unlike the other C*Pointer types because it only needs to reference the results of inout conversions, which already have writeback-scoped lifetime.

## Topics

### Converting Pointers
- [init?<U>(UnsafeMutablePointer<U>?)](autoreleasingunsafemutablepointer/init(_:)-7rndr.md)
  Explicit construction from an UnsafeMutablePointer.
- [init<U>(UnsafeMutablePointer<U>)](autoreleasingunsafemutablepointer/init(_:)-4mrz1.md)
  Explicit construction from an UnsafeMutablePointer.
### Accessing a Pointer’s Memory
- [var pointee: Pointee](autoreleasingunsafemutablepointer/pointee.md)
  Retrieve or set the `Pointee` instance referenced by `self`.
- [subscript(Int) -> Pointee](autoreleasingunsafemutablepointer/subscript(_:).md)
  Access the `i`th element of the raw array pointed to by `self`.
### Comparing Pointers
- [static func == (Self, Self) -> Bool](autoreleasingunsafemutablepointer/==(_:_:)-4wfti.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](autoreleasingunsafemutablepointer/!=(_:_:)-1bazr.md)
  Returns a Boolean value indicating whether two values are not equal.
### Instance Properties
- [var hashValue: Int](autoreleasingunsafemutablepointer/hashvalue.md)
  The hash value.
### Type Aliases
- [AutoreleasingUnsafeMutablePointer.Stride](autoreleasingunsafemutablepointer/stride.md)
  A type that represents the distance between two values.
### Default Implementations
- [Comparable Implementations](autoreleasingunsafemutablepointer/comparable-implementations.md)
- [CustomReflectable Implementations](autoreleasingunsafemutablepointer/customreflectable-implementations.md)
- [Equatable Implementations](autoreleasingunsafemutablepointer/equatable-implementations.md)
- [Hashable Implementations](autoreleasingunsafemutablepointer/hashable-implementations.md)
- [Strideable Implementations](autoreleasingunsafemutablepointer/strideable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [CVarArg](cvararg.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Strideable](strideable.md)

## See Also

- [struct OpaquePointer](opaquepointer.md)
  A wrapper around an opaque C pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer)*