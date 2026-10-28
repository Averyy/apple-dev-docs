# iterateObjects

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Iterates the array calling a callback block for each member.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool iterateObjects(OSCollectionIterateObjectsBlock block) const;
```

## Return Value

False if the callback block returned false, otherwise true (including if the array is empty).

## Discussion

Calls the block with each member of the array, starting at index zero. The block must not modify the array during iteration. If the block returns true the iteration continues for all members, returning false halts the iteration early.

## Parameters

- `block`: The block to invoke.

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
- [replaceObject](./replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](./removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](../osarrayappendvalue.md)
- [OSArrayReplaceValue](../osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/iterateobjects)*