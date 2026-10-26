# NSPointerArray

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A collection similar to an array, but with a broader range of available memory semantics.

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
class NSPointerArray
```

```objc
@interface NSPointerArray : NSObject
```

#### Overview

The pointer array class is modeled after [`NSArray`](./nsarray.md), but can also hold `nil` values. You can insert or remove `nil` values which contribute to the array’s [`count`](./nspointerarray/count.md).

A pointer array can be initialized to maintain strong or weak references to objects, or according to any of the memory or personality options defined by [`NSPointerFunctions.Options`](./nspointerfunctions/options.md).

The [`NSCopying`](./nscopying.md) and [`NSCoding`](./nscoding.md) protocols are applicable only when a pointer array is initialized to maintain strong or weak references to objects.

When enumerating a pointer array with [`NSFastEnumeration`](./nsfastenumeration.md) using `for...in`, the loop will yield any `nil` values present in the array. See [Fast Enumeration Makes It Easy to Enumerate a Collection](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/FoundationTypesandCollections/FoundationTypesandCollections.html#//apple_ref/doc/uid/TP40011210-CH7-SW30) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210) for more information.

##### Subclassing Notes

`NSPointerArray` is not suitable for subclassing.

## Topics

### Creating and Initializing a New Pointer Array
- [init(options: NSPointerFunctions.Options)](./nspointerarray/init%28options%29.md)
  Initializes the receiver to use the given options.
- [init(pointerFunctions: NSPointerFunctions)](./nspointerarray/init%28pointerfunctions%29.md)
  Initializes the receiver to use the given functions.
- [class func strongObjects() -> NSPointerArray](./nspointerarray/strongobjects%28%29.md)
  Returns a new pointer array that maintains strong references to its elements.
- [class func weakObjects() -> NSPointerArray](./nspointerarray/weakobjects%28%29.md)
  Returns a new pointer array that maintains weak references to its elements.
- [+ pointerArrayWithOptions:](./nspointerarray/pointerarraywithoptions_.md)
  Returns a new pointer array initialized to use the given options.
- [+ pointerArrayWithPointerFunctions:](./nspointerarray/pointerarraywithpointerfunctions_.md)
  A new pointer array initialized to use the given functions.
- [+ pointerArrayWithStrongObjects](./nspointerarray/pointerarraywithstrongobjects.md)
  Returns a new pointer array that maintains strong references to its elements.
- [+ pointerArrayWithWeakObjects](./nspointerarray/pointerarraywithweakobjects.md)
  Returns a new pointer array that maintains weak references to its elements.
### Managing the Collection
- [var count: Int](./nspointerarray/count.md)
  The number of elements in the receiver.
- [var allObjects: [Any]](./nspointerarray/allobjects.md)
  All the objects in the receiver.
- [func pointer(at: Int) -> UnsafeMutableRawPointer?](./nspointerarray/pointer%28at%29.md)
  Returns the pointer at a given index.
- [func addPointer(UnsafeMutableRawPointer?)](./nspointerarray/addpointer%28_%29.md)
  Adds a given pointer to the receiver.
- [func removePointer(at: Int)](./nspointerarray/removepointer%28at%29.md)
  Removes the pointer at a given index.
- [func insertPointer(UnsafeMutableRawPointer?, at: Int)](./nspointerarray/insertpointer%28_,at%29.md)
  Inserts a pointer at a given index.
- [func replacePointer(at: Int, withPointer: UnsafeMutableRawPointer?)](./nspointerarray/replacepointer%28at,withpointer%29.md)
  Replaces the pointer at a given index.
- [func compact()](./nspointerarray/compact%28%29.md)
  Removes `NULL` values from the receiver.
### Getting the Pointer Functions
- [var pointerFunctions: NSPointerFunctions](./nspointerarray/pointerfunctions.md)
  The functions in use by the receiver.
- [class NSPointerFunctions](./nspointerfunctions.md)
  An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.
### Initializers
- [init?(coder: NSCoder)](./nspointerarray/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Pointer Collections
- [class NSMapTable](./nsmaptable.md)
  A collection similar to a dictionary, but with a broader range of available memory semantics.
- [class NSHashTable](./nshashtable.md)
  A collection similar to a set, but with broader range of available memory semantics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray)*