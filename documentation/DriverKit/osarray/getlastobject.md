# getLastObject

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the last member of the array.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
OSObject * getLastObject() const;
```

## Return Value

Member at the last index or NULL if array has no members.

## Discussion

If the array has non-zero count the member at the last index is returned, with no additional retain count (the caller should not release). Otherwise NULL.

## See Also

### Accessing Elements
- [getObject](./getobject.md)
  Returns a member of the array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/getlastobject)*