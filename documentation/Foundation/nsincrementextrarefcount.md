# NSIncrementExtraRefCount

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Increments the specified object’s reference count.

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
extern void NSIncrementExtraRefCount(id object);
```

#### Discussion

This function increments the “extra reference” count of `object`. Newly created objects have only one actual reference, so that a single release message results in the object being deallocated. Extra references are those beyond the single original reference and are usually created by sending the object a retain message. Your code should generally not use these functions unless it is overriding the retain or release methods.

##### Special Considerations

This function is deprecated and unavailable for use with ARC.

## Parameters

- `object`: An object.

## See Also

### Object Allocation and Deallocation
- [NSAllocateObject](./nsallocateobject.md)
  Creates and returns a new instance of a given class.
- [NSCopyObject](./nscopyobject.md)
  Creates an exact copy of an object.
- [NSDeallocateObject](./nsdeallocateobject.md)
  Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](./nsdecrementextrarefcountwaszero.md)
  Decrements the specified object’s reference count.
- [NSExtraRefCount](./nsextrarefcount.md)
  Returns the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsincrementextrarefcount)*