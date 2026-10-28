# OpaquePointer

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A wrapper around an opaque C pointer.

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
struct OpaquePointer
```

## Overview

Opaque pointers are used to represent C pointers to types that cannot be represented in Swift, such as incomplete struct types.

## Topics

### Initializers
- [init(UnsafeRawPointer)](./opaquepointer/init%28_%29-3h8av.md)
- [init?(UnsafeMutableRawPointer?)](./opaquepointer/init%28_%29-4g6sp.md)
- [init<T>(UnsafePointer<T>)](./opaquepointer/init%28_%29-4u1ar.md)
  Converts a typed `UnsafePointer` to an opaque C pointer.
- [init?(UnsafeRawPointer?)](./opaquepointer/init%28_%29-6gmth.md)
- [init<T>(UnsafeMutablePointer<T>)](./opaquepointer/init%28_%29-7oa0u.md)
  Converts a typed `UnsafeMutablePointer` to an opaque C pointer.
- [init(UnsafeMutableRawPointer)](./opaquepointer/init%28_%29-7zxvo.md)
- [init?<T>(UnsafePointer<T>?)](./opaquepointer/init%28_%29-b58i.md)
  Converts a typed `UnsafePointer` to an opaque C pointer.
- [init?<T>(UnsafeMutablePointer<T>?)](./opaquepointer/init%28_%29-xapj.md)
  Converts a typed `UnsafeMutablePointer` to an opaque C pointer.
- [init?(bitPattern: Int)](./opaquepointer/init%28bitpattern%29-26uvs.md)
  Creates a new `OpaquePointer` from the given address, specified as a bit pattern.
- [init?(bitPattern: UInt)](./opaquepointer/init%28bitpattern%29-7f8tm.md)
  Creates a new `OpaquePointer` from the given address, specified as a bit pattern.
### Instance Properties
- [var intendedSpatialExperience: any SpatialAudioExperience](./opaquepointer/intendedspatialexperience.md)
  The AudioQueue’s intended spatial audio experience.
### Default Implementations
- [AtomicOptionalRepresentable Implementations](./opaquepointer/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](./opaquepointer/atomicrepresentable-implementations.md)
- [CustomDebugStringConvertible Implementations](./opaquepointer/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](./opaquepointer/equatable-implementations.md)
- [Hashable Implementations](./opaquepointer/hashable-implementations.md)

## Relationships

### Conforms To
- [AtomicOptionalRepresentable](../Synchronization/atomicoptionalrepresentable.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [CVarArg](./cvararg.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [Copyable](./copyable.md)
- [CustomDebugStringConvertible](./customdebugstringconvertible.md)
- [Equatable](./equatable.md)
- [Escapable](./escapable.md)
- [Hashable](./hashable.md)

## See Also

### C and Objective-C Pointers
- [struct AutoreleasingUnsafeMutablePointer](./autoreleasingunsafemutablepointer.md)
  A mutable pointer addressing an Objective-C reference that doesn’t own its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/opaquepointer)*