# merge

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Adds all members of a dictionary to this dictionary.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool merge(const OSDictionary *otherDictionary);
```

## Return Value

True on success, which retains all the added objects, or false on failure which does not retain the objects.

## Discussion

Adds all members of a dictionary to this dictionary. Any keys in the dictionary that exist will be replaced. The dictionary capacity will be grown if necessary.

## Parameters

- `otherDictionary`: All members of thie dictionary will be added to the array.

## See Also

### Creating a Dictionary
- [withCapacity](./withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [withDictionary](./withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [withObjects](./withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [OSDictionaryCreate](../osdictionarycreate.md)
- [free](./free.md)
- [flushCollection](./flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/merge)*