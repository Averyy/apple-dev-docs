# ObjectIdentifier

**Framework**: Swift  
**Kind**: struct

A unique identifier for a class instance or metatype.

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
struct ObjectIdentifier
```

#### Overview

This unique identifier is only valid for comparisons during the lifetime of the instance.

In Swift, only class instances and metatypes have unique identities. There is no notion of identity for structs, enums, functions, or tuples.

## Topics

### Initializers
- [init(AnyObject)](objectidentifier/init(_:)-223xw.md)
  Creates an instance that uniquely identifies the given class instance.
- [init(any (~Copyable & ~Escapable).Type)](objectidentifier/init(_:)-52bz1.md)
  Creates an instance that uniquely identifies the given metatype.
- [init(any Any.Type)](objectidentifier/init(_:)-86u7l.md)
### Default Implementations
- [AtomicOptionalRepresentable Implementations](objectidentifier/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](objectidentifier/atomicrepresentable-implementations.md)
- [Comparable Implementations](objectidentifier/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](objectidentifier/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](objectidentifier/equatable-implementations.md)
- [Hashable Implementations](objectidentifier/hashable-implementations.md)

## Relationships

### Conforms To
- [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Mirror](mirror.md)
  A representation of the substructure and display style of an instance of any type.
- [func type<T, Metatype>(of: borrowing T) -> Metatype](type(of:).md)
  Returns the dynamic type of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/objectidentifier)*