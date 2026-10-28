# getObject

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a member of the array.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
OSObject * getObject(uint32_t index) const;
```

## Return Value

Member at the given index or NULL if the index is greater or equal to the array count. The retain count of the result object is not incremented and the object should not be release by the caller.

## Discussion

If the index is less than the array count the member at that index is returned, with no additional retain count (the caller should not release). Otherwise NULL.

## Parameters

- `index`: Zero based index less than the array count to add the object.

## See Also

### Accessing Elements
- [getLastObject](./getlastobject.md)
  Returns the last member of the array.
- [getNextIndexOfObject](./getnextindexofobject.md)
  Searches the array for an object.
- [setObject](./setobject-3bore.md)
  Appends an object as the last member of the array.
- [setObject](./setobject-4ys3x.md)
  Sets an object as the member of the array at a given index.
- [iterateObjects](./iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [replaceObject](./replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](./removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](../osarrayappendvalue.md)
- [OSArrayReplaceValue](../osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/getobject)*