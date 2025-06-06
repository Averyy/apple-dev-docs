# OSCollection

**Framework**: DriverKit  
**Kind**: class

The base class for DriverKit collection objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSCollection;
```

## Topics

### Inspecting a Collection
- [getCount](oscollection/getcount.md)
- [getCapacity](oscollection/getcapacity.md)
- [ensureCapacity](oscollection/ensurecapacity.md)
### Accessing Collection Elements
- [iterateObjects](oscollection/iterateobjects.md)
- [flushCollection](oscollection/flushcollection.md)
- [OSCollectionIterateObjectsBlock](oscollectioniterateobjectsblock.md)
### Copying the Collection
- [copyCollection](oscollection/copycollection.md)
- [OSCollectionPtr](oscollectionptr.md)
### Getting Type Information
- [OSCollectionTypeID](oscollectiontypeid.md)
- [OSCollectionTypeName](oscollectiontypename.md)
- [Collection Types](3180990-collection_types.md)
- [OSCollectionType](oscollectiontype.md)
### Initializing Collection Types
- [OSCollectionsInitialize](oscollectionsinitialize.md)

## Relationships

### Inherits From
- [OSContainer](oscontainer.md)
### Inherited By
- [OSArray](osarray.md)
- [OSDictionary](osdictionary.md)

## See Also

- [OSArray](osarray.md)
  A container for an ordered, random-access collection of objects.
- [OSDictionary](osdictionary.md)
  A container for a collection with elements that are key-value pairs.
- [OSBoolean](osboolean.md)
  A container for a true or false value.
- [OSData](osdata.md)
  A container for untyped data.
- [OSNumber](osnumber.md)
  A container for an integer value.
- [OSString](osstring.md)
  A container for managing an array of characters.
- [OSSerialization](osserialization.md)
  A container for one or more objects, serialized in a binary data format that is suitable for messaging.
- [OSContainer](oscontainer.md)
  The base class for DriverKit data objects.
- [OSObject](osobject.md)
  The base class for DriverKit objects
- [OSSymbol](ossymbol.md)
  A container for managing an array of characters.
- [IOFixed](iofixed.md)
  A fixed-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/oscollection)*