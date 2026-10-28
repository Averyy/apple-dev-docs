# NSAllocateObject

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Creates and returns a new instance of a given class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern idNSAllocateObject(Class aClass, NSUInteger extraBytes, NSZone *zone);
```

## Return Value

A new instance of `aClass` or `nil` if an instance could not be created.

## Discussion

This function is deprecated and unavailable for use with ARC.

## Parameters

- `aClass`: The class of which to create an instance.
- `extraBytes`: The number of extra bytes required for indexed instance variables (this value is typically `0`).
- `zone`: The zone in which to create the new instance (pass `NULL` to specify the default zone).

## See Also

### Object Allocation and Deallocation
- [NSCopyObject](./nscopyobject.md)
  Creates an exact copy of an object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsallocateobject)*