# NSDeallocateObject

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Destroys an existing object.

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
extern void NSDeallocateObject(id object);
```

## Discussion

This function deallocates `object`, which must have been allocated using `NSAllocateObject`.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## Parameters

- `object`: An object.

## See Also

### Object Allocation and Deallocation
- [NSAllocateObject](./nsallocateobject.md)
  Creates and returns a new instance of a given class.
- [NSCopyObject](./nscopyobject.md)
  Creates an exact copy of an object.
- [NSDecrementExtraRefCountWasZero](./nsdecrementextrarefcountwaszero.md)
  Decrements the specified object’s reference count.
- [NSExtraRefCount](./nsextrarefcount.md)
  Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeallocateobject)*