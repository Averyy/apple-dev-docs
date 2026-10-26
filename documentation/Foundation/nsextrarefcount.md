# NSExtraRefCount

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the specified object’s reference count.

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
extern NSUInteger NSExtraRefCount(id object);
```

#### Return Value

The current reference count of `object`.

#### Discussion

This function is used in conjunction with [`NSIncrementExtraRefCount`](./nsincrementextrarefcount.md) and [`NSDecrementExtraRefCountWasZero`](./nsdecrementextrarefcountwaszero.md) in situations where you need to override an object’s [`retain`](../ObjectiveC/nsobject-c.protocol/retain.md) and [`release`](../ObjectiveC/nsobject-c.protocol/release.md) methods.

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
- [NSIncrementExtraRefCount](./nsincrementextrarefcount.md)
  Increments the specified object’s reference count.
- [NSShouldRetainWithZone](./nsshouldretainwithzone.md)
  Indicates whether an object should be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextrarefcount)*