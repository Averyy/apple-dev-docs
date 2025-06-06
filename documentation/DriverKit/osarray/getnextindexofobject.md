# getNextIndexOfObject

**Framework**: DriverKit  
**Kind**: method

Searches the array for an object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint32_t getNextIndexOfObject(const OSMetaClassBase * anObject, uint32_t index) const;
```

#### Return Value

Index at which the object was found, or -1U if the member was not found in the array after the index parameter.

#### Discussion

Beginning at the passed index, iterate the array until the object instance is found or there are no more members. The search is done by pointer equality.

## Parameters

- `anObject`: The object to search for.
- `index`: Zero based index less than the array count to begin the search.

## See Also

- [getObject](osarray/getobject.md)
  Returns a member of the array.
- [getLastObject](osarray/getlastobject.md)
  Returns the last member of the array.
- [setObject](osarray/setobject-3bore.md)
  Appends an object as the last member of the array.
- [setObject](osarray/setobject-4ys3x.md)
  Sets an object as the member of the array at a given index.
- [iterateObjects](osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [replaceObject](osarray/replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](osarray/removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](osarrayappendvalue.md)
- [OSArrayReplaceValue](osarrayreplacevalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/getnextindexofobject)*