# NSPointerArray

**Framework**: Foundation  
**Kind**: class

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

#### Overview

The pointer array class is modeled after [`NSArray`](nsarray.md), but can also hold `nil` values. You can insert or remove `nil` values which contribute to the array’s [`count`](nspointerarray/count.md).

A pointer array can be initialized to maintain strong or weak references to objects, or according to any of the memory or personality options defined by [`NSPointerFunctions.Options`](nspointerfunctions/options.md).

The [`NSCopying`](nscopying.md) and [`NSCoding`](nscoding.md) protocols are applicable only when a pointer array is initialized to maintain strong or weak references to objects.

When enumerating a pointer array with [`NSFastEnumeration`](nsfastenumeration.md) using `for...in`, the loop will yield any `nil` values present in the array. See [`Fast Enumeration Makes It Easy to Enumerate a Collection`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/FoundationTypesandCollections/FoundationTypesandCollections.html#//apple_ref/doc/uid/TP40011210-CH7-SW30) in [`Programming with Objective-C`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210) for more information.

##### Subclassing Notes

`NSPointerArray` is not suitable for subclassing.

## Topics

### Creating and Initializing a New Pointer Array
- [init(options: NSPointerFunctions.Options)](nspointerarray/init(options:).md)
  Initializes the receiver to use the given options.
- [init(pointerFunctions: NSPointerFunctions)](nspointerarray/init(pointerfunctions:).md)
  Initializes the receiver to use the given functions.
- [class func strongObjects() -> NSPointerArray](nspointerarray/strongobjects.md)
  Returns a new pointer array that maintains strong references to its elements.
- [class func weakObjects() -> NSPointerArray](nspointerarray/weakobjects.md)
  Returns a new pointer array that maintains weak references to its elements.
### Managing the Collection
- [var count: Int](nspointerarray/count.md)
  The number of elements in the receiver.
- [var allObjects: [Any]](nspointerarray/allobjects.md)
  All the objects in the receiver.
- [func pointer(at: Int) -> UnsafeMutableRawPointer?](nspointerarray/pointer(at:).md)
  Returns the pointer at a given index.
- [func addPointer(UnsafeMutableRawPointer?)](nspointerarray/addpointer(_:).md)
  Adds a given pointer to the receiver.
- [func removePointer(at: Int)](nspointerarray/removepointer(at:).md)
  Removes the pointer at a given index.
- [func insertPointer(UnsafeMutableRawPointer?, at: Int)](nspointerarray/insertpointer(_:at:).md)
  Inserts a pointer at a given index.
- [func replacePointer(at: Int, withPointer: UnsafeMutableRawPointer?)](nspointerarray/replacepointer(at:withpointer:).md)
  Replaces the pointer at a given index.
- [func compact()](nspointerarray/compact.md)
  Removes `NULL` values from the receiver.
### Getting the Pointer Functions
- [var pointerFunctions: NSPointerFunctions](nspointerarray/pointerfunctions.md)
  The functions in use by the receiver.
- [class NSPointerFunctions](nspointerfunctions.md)
  An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class NSMapTable](nsmaptable.md)
  A collection similar to a dictionary, but with a broader range of available memory semantics.
- [class NSHashTable](nshashtable.md)
  A collection similar to a set, but with broader range of available memory semantics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray)*