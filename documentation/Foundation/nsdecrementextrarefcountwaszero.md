# NSDecrementExtraRefCountWasZero

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Decrements the specified object’s reference count.

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
extern BOOL NSDecrementExtraRefCountWasZero(id object);
```

## Return Value

[`false`](../Swift/false.md) if `anObject` had an extra reference count, or [`true`](../Swift/true.md) if `anObject` didn’t have an extra reference count—indicating that the object should be deallocated (with `dealloc`).

## Discussion

Decrements the “extra reference” count of `anObject`. Newly created objects have only one actual reference, so that a single release message results in the object being deallocated. Extra references are those beyond the single original reference and are usually created by sending the object a retain message. Your code should generally not use these functions unless it is overriding the [`retain`](../ObjectiveC/nsobject-c.protocol/retain.md) or [`release`](../ObjectiveC/nsobject-c.protocol/release.md) methods.

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
- [NSDeallocateObject](./nsdeallocateobject.md)
  Destroys an existing object.
- [NSExtraRefCount](./nsextrarefcount.md)
  Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecrementextrarefcountwaszero)*