# getObject

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a member of the dictionary.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
OSObject * getObject(const OSObject *aKey) const;
```

#### Return Value

Member at the given index or NULL if the index is greater or equal to the array count. The retain count of the result object is not incremented and the object should not be release by the caller.

#### Discussion

Looks up an existing object in the dictionary with the given key and returns it.

## Parameters

- `aKey`: An object pointer used to lookup the object. The key should be uniqued within the dictionary. Usually an OSString is passed as the key.

## See Also

### Accessing Keys and Values
- [getObject](./getobject-8k3ie.md)
  Returns a member of the dictionary.
- [setObject](./setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [setObject](./setobject-7q0u2.md)
  Add or replace an object in the dictionary.
- [removeObject](./removeobject-25qm5.md)
  Remove an object by key from the dictionary.
- [removeObject](./removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [iterateObjects](./iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [iterateObjects](./iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](../osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](../osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/getobject-9ikoz)*