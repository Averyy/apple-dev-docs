# NSPointerFunctions

**Framework**: Foundation  
**Kind**: class

An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSPointerFunctions
```

#### Overview

The functions specified by an instance of `NSPointerFunctions` are separated into two clusters—those that define “personality” such as “object” or “C-string”, and those that describe memory management issues such as a memory deallocation function. There are constants for common personalities and memory manager selections (see `Memory and Personality Options`).

[`NSHashTable`](nshashtable.md), [`NSMapTable`](nsmaptable.md), and [`NSPointerArray`](nspointerarray.md) use an `NSPointerFunctions` object to define the acquisition and retention behavior for the pointers they manage. Note, however, that not all combinations of personality and memory management behavior are valid for these collections. The pointer collection objects copy the `NSPointerFunctions` object on input and output, so you cannot usefully subclass `NSPointerFunctions`.

##### Subclassing Notes

`NSPointerFunctions` is not suitable for subclassing.

## Topics

### Creating and Initializing an NSPointerFunctions Object
- [init(options: NSPointerFunctions.Options)](nspointerfunctions/init(options:).md)
  Returns an `NSPointerFunctions` object initialized with the given options.
### Personality Functions
- [var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)?](nspointerfunctions/hashfunction.md)
  The hash function.
- [var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)?](nspointerfunctions/isequalfunction.md)
  The function used to compare pointers.
- [var sizeFunction: ((UnsafeRawPointer) -> Int)?](nspointerfunctions/sizefunction.md)
  The function used to determine the size of pointers.
- [var descriptionFunction: ((UnsafeRawPointer) -> String?)?](nspointerfunctions/descriptionfunction.md)
  The function used to describe elements.
### Memory Configuration
- [var acquireFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?, ObjCBool) -> UnsafeMutableRawPointer)?](nspointerfunctions/acquirefunction.md)
  The function used to acquire memory.
- [var relinquishFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Void)?](nspointerfunctions/relinquishfunction.md)
  The function used to relinquish memory.
- [var usesStrongWriteBarrier: Bool](nspointerfunctions/usesstrongwritebarrier.md)
  Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier.
- [var usesWeakReadAndWriteBarriers: Bool](nspointerfunctions/usesweakreadandwritebarriers.md)
  Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers.
### Constants
- [NSPointerFunctions.Options](nspointerfunctions/options.md)
  Defines the memory and personality options for an `NSPointerFunctions` object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var pointerFunctions: NSPointerFunctions](nshashtable/pointerfunctions.md)
  The pointer functions for the hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions)*