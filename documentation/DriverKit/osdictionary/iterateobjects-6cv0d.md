# iterateObjects

**Framework**: DriverKit  
**Kind**: method

Iterates the dictionary calling a callback block for each member.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool iterateObjects(OSCollectionIterateObjectsBlockblock) const;
```

#### Return Value

False if the callback block returned false, otherwise true (including if the array is empty).

#### Discussion

Calls the block with each member of the dictionary. The block must not dictionary the array during iteration. If the block returns true the iteration continues for all members, returning false halts the iteration early. OSDictionary also has a dictionary specific iterateObjects() which supplies the key and value to the callback.

## Parameters

- `block`: The block to invoke.

## See Also

- [getObject](osdictionary/getobject-9ikoz.md)
  Returns a member of the dictionary.
- [getObject](osdictionary/getobject-8k3ie.md)
  Returns a member of the dictionary.
- [setObject](osdictionary/setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [setObject](osdictionary/setobject-7q0u2.md)
  Add or replace an object in the dictionary.
- [removeObject](osdictionary/removeobject-25qm5.md)
  Remove an object by key from the dictionary.
- [removeObject](osdictionary/removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [iterateObjects](osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/iterateobjects-6cv0d)*