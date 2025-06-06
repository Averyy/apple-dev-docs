# setObject

**Framework**: DriverKit  
**Kind**: method

Add or replace an object in the dictionary.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool setObject(const char * aKey, const OSMetaClassBase * anObject);
```

#### Return Value

True on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

The object is added to the dictionary with the key object. If an object with the given key existed prior to the call it is replaced and released. The dictionary capacity will be grown if necessary.

## Parameters

- `aKey`: A c-string key. An OSString is created from aKey and used as the key for the dictionary.
- `anObject`: Object to be added to the dictionary.

## See Also

- [getObject](osdictionary/getobject-9ikoz.md)
  Returns a member of the dictionary.
- [getObject](osdictionary/getobject-8k3ie.md)
  Returns a member of the dictionary.
- [setObject](osdictionary/setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [removeObject](osdictionary/removeobject-25qm5.md)
  Remove an object by key from the dictionary.
- [removeObject](osdictionary/removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [iterateObjects](osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [iterateObjects](osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/setobject-7q0u2)*