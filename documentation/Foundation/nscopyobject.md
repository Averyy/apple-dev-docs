# NSCopyObject

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Creates an exact copy of an object.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```c
extern idNSCopyObject(id object, NSUInteger extraBytes, NSZone *zone);
```

## Return Value

A new object that’s an exact copy of `anObject`, or `nil` if `object` is `nil` or if `object` could not be copied.

## Discussion

This function is deprecated and unavailable for use with ARC. To create a copy of an object, use the [`copyWithZone:`](../ObjectiveC/nsobject-swift.class/copywithzone_.md) method instead.

## Parameters

- `object`: The object to copy.
- `extraBytes`: The number of extra bytes required for indexed instance variables (this value is typically `0`).
- `zone`: The zone in which to create the new instance (pass `NULL` to specify the default zone).

## See Also

### Object Allocation and Deallocation
- [NSAllocateObject](./nsallocateobject.md)
  Creates and returns a new instance of a given class.
- [NSDeallocateObject](./nsdeallocateobject.md)
  Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](./nsdecrementextrarefcountwaszero.md)
  Decrements the specified object’s reference count.
- [NSExtraRefCount](./nsextrarefcount.md)
  Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscopyobject)*