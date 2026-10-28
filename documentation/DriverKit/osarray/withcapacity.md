# withCapacity

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Allocates an OSArray object with preallocated capacity.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSArrayPtr withCapacity(uint32_t capacity);
```

## Return Value

NULL on failure, otherwise the allocated OSArray with reference count 1 to be released by the caller.

## Parameters

- `capacity`: Count of allocated capacity for members in array.

## See Also

### Creating an Array
- [withArray](./witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [withObjects](./withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [OSArrayCreate](../osarraycreate.md)
- [merge](./merge.md)
  Appends all members of an array to this array.
- [free](./free.md)
- [flushCollection](./flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/withcapacity)*