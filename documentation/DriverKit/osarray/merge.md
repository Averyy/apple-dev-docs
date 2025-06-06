# merge

**Framework**: DriverKit  
**Kind**: method

Appends all members of an array to this array.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool merge(const OSArray * otherArray);
```

#### Return Value

True on success, which retains all the added objects, or false on failure which does not retain the objects.

#### Discussion

Appends all members of an array to this array. The array capacity will be grown if necessary.

## Parameters

- `otherArray`: All members of thie array will be appended to the array.

## See Also

- [withArray](osarray/witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [withCapacity](osarray/withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [withObjects](osarray/withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [OSArrayCreate](osarraycreate.md)
- [free](osarray/free.md)
- [flushCollection](osarray/flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/merge)*