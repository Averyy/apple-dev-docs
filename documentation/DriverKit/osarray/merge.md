# merge

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Appends all members of an array to this array.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool merge(const OSArray *otherArray);
```

#### Return Value

True on success, which retains all the added objects, or false on failure which does not retain the objects.

#### Discussion

Appends all members of an array to this array. The array capacity will be grown if necessary.

## Parameters

- `otherArray`: All members of thie array will be appended to the array.

## See Also

### Creating an Array
- [withArray](./witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [withCapacity](./withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [withObjects](./withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [OSArrayCreate](../osarraycreate.md)
- [free](./free.md)
- [flushCollection](./flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/merge)*