# iterateObjects

**Framework**: DriverKit  
**Kind**: method

Iterates the array calling a callback block for each member.

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

Calls the block with each member of the array, starting at index zero. The block must not modify the array during iteration. If the block returns true the iteration continues for all members, returning false halts the iteration early.

## Parameters

- `block`: The block to invoke.

## See Also

- [getObject](osarray/getobject.md)
  Returns a member of the array.
- [getLastObject](osarray/getlastobject.md)
  Returns the last member of the array.
- [getNextIndexOfObject](osarray/getnextindexofobject.md)
  Searches the array for an object.
- [setObject](osarray/setobject-3bore.md)
  Appends an object as the last member of the array.
- [setObject](osarray/setobject-4ys3x.md)
  Sets an object as the member of the array at a given index.
- [replaceObject](osarray/replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](osarray/removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](osarrayappendvalue.md)
- [OSArrayReplaceValue](osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/iterateobjects)*