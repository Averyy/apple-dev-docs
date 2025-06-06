# setObject

**Framework**: DriverKit  
**Kind**: method

Sets an object as the member of the array at a given index.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool setObject(uint32_t index, const OSMetaClassBase * anObject);
```

#### Return Value

True on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

Sets an object as the member of the array at a given index. The array capacity will be grown if necessary.

## Parameters

- `index`: Zero based index less than or equal to the array count to add the object.
- `anObject`: Object to be added to the array.

## See Also

- [getObject](osarray/getobject.md)
  Returns a member of the array.
- [getLastObject](osarray/getlastobject.md)
  Returns the last member of the array.
- [getNextIndexOfObject](osarray/getnextindexofobject.md)
  Searches the array for an object.
- [setObject](osarray/setobject-3bore.md)
  Appends an object as the last member of the array.
- [iterateObjects](osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [replaceObject](osarray/replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](osarray/removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](osarrayappendvalue.md)
- [OSArrayReplaceValue](osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/setobject-4ys3x)*