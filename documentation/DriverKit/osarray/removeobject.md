# removeObject

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Removes a current member of the array.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
void removeObject(uint32_t index);
```

## Discussion

Removes a current member of the array, shifting down all following members. The removed object is released.

## Parameters

- `index`: Zero based index less than the array count of the object to remove.

## See Also

### Accessing Elements
- [getObject](./getobject.md)
  Returns a member of the array.
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
- [OSArrayAppendValue](../osarrayappendvalue.md)
- [OSArrayReplaceValue](../osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/removeobject)*