# NSShouldRetainWithZone

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Indicates whether an object should be retained.

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
extern BOOL NSShouldRetainWithZone(id anObject, NSZone *requestedZone);
```

## Return Value

Returns [`true`](../Swift/true.md) if `requestedZone` is `NULL`, the default zone, or the zone in which `anObject` was allocated; otherwise [`false`](../Swift/false.md).

## Discussion

This function is typically called from inside an `NSObject`’s [`copyWithZone:`](../ObjectiveC/nsobject-swift.class/copywithzone_.md), when deciding whether to retain `anObject` as opposed to making a copy of it.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## Parameters

- `anObject`: An object.
- `requestedZone`: A memory zone.

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
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsshouldretainwithzone)*