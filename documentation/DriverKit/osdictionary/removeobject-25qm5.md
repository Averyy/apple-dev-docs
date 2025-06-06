# removeObject

**Framework**: DriverKit  
**Kind**: method

Remove an object by key from the dictionary.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void removeObject(const OSObject * aKey);
```

#### Discussion

An object in the dictionary with the given key object is removed and released.

## Parameters

- `aKey`: An object pointer used to lookup the object. The key should be uniqued within the dictionary. Usually an OSString is passed as the key.

## See Also

- [getObject](osdictionary/getobject-9ikoz.md)
  Returns a member of the dictionary.
- [getObject](osdictionary/getobject-8k3ie.md)
  Returns a member of the dictionary.
- [setObject](osdictionary/setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [setObject](osdictionary/setobject-7q0u2.md)
  Add or replace an object in the dictionary.
- [removeObject](osdictionary/removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [iterateObjects](osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [iterateObjects](osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/removeobject-25qm5)*