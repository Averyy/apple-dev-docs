# withDictionary

**Framework**: DriverKit  
**Kind**: method

Allocates an OSDictionary object with given members and preallocated capacity.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSDictionaryPtr withDictionary(const OSDictionary * dictionary, uint32_t capacity);
```

#### Return Value

NULL on failure, otherwise the allocated OSDictionary with reference count 1 to be released by the caller.

## Parameters

- `dictionary`: Dictionary object containing members for the new dictionary.
- `capacity`: Count of allocated capacity for members in array.

## See Also

- [withCapacity](osdictionary/withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [withObjects](osdictionary/withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [OSDictionaryCreate](osdictionarycreate.md)
- [merge](osdictionary/merge.md)
  Adds all members of a dictionary to this dictionary.
- [free](osdictionary/free.md)
- [flushCollection](osdictionary/flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/withdictionary)*