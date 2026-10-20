# iterateObjects

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Iterates the dictionary calling a callback block for each member.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool iterateObjects(OSDictionaryIterateObjectsBlock block) const;
```

#### Return Value

False if the callback block returned false, otherwise true (including if the dictionary is empty).

#### Discussion

Calls the block with each value in the dictionary. The block must not modify the dictionary during iteration. If the block returns true the iteration continues for all members, returning false halts the iteration early.

## Parameters

- `block`: The block to invoke.

## See Also

### Accessing Keys and Values
- [getObject](./getobject-9ikoz.md)
  Returns a member of the dictionary.
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
- [iterateObjects](./iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](../osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](../osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/iterateobjects-9h89s)*