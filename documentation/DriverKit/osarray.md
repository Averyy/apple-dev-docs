# OSArray

**Framework**: DriverKit  
**Kind**: class

A container for an ordered, random-access collection of objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSArray;
```

#### Overview

OSArray is a collection class for objects derived from OSObject. Storage and access are by array index.

You must generally cast retrieved objects from OSObject to the desired class using the OSDynamicCast macro. This macro returns the object cast to the desired class, or `NULL` if the object isn’t derived from that class.

As with all DriverKit collection classes, OSArray retains objects added to it, and releases objects removed from it (or replaced). An OSArray also grows as necessary to accommodate new objects.

OSArray provides no concurrency protection; it’s up to the usage context to provide any protection necessary.

## Topics

### Creating an Array
- [withArray](osarray/witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [withCapacity](osarray/withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [withObjects](osarray/withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [OSArrayCreate](osarraycreate.md)
- [merge](osarray/merge.md)
  Appends all members of an array to this array.
- [free](osarray/free.md)
- [flushCollection](osarray/flushcollection.md)
  Removes and drops references to all members of array.
### Accessing Elements
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
- [iterateObjects](osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [replaceObject](osarray/replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [removeObject](osarray/removeobject.md)
  Removes a current member of the array.
- [OSArrayAppendValue](osarrayappendvalue.md)
- [OSArrayReplaceValue](osarrayreplacevalue.md)
### Getting and Setting Values
- [OSArrayGetValue](osarraygetvalue.md)
- [OSArrayGetStringValue](osarraygetstringvalue.md)
- [OSArrayGetUInt64Value](osarraygetuint64value.md)
- [OSArraySetValue](osarraysetvalue.md)
- [OSArraySetStringValue](osarraysetstringvalue.md)
- [OSArraySetUInt64Value](osarraysetuint64value.md)
- [Array Indices](3180989-array_indices.md)
- [OSArrayPtr](osarrayptr.md)
### Inspecting an Array
- [getCount](osarray/getcount.md)
  Returns count of members in array.
- [getCapacity](osarray/getcapacity.md)
  Returns count of currently allocated capacity for members in array.
- [ensureCapacity](osarray/ensurecapacity.md)
  Allocates capacity for members in array.
- [OSArrayGetCount](osarraygetcount.md)
### Modifying the Array Contents
- [OSArrayApply](osarrayapply.md)
- [OSArrayApplier](osarrayapplier.md)
### Comparing Arrays
- [isEqualTo](osarray/isequalto-5w7om.md)
  Compares all members of two arrays with isEqualTo().
- [isEqualTo](osarray/isequalto-93qxy.md)
  Compares the array with an OSObject

## Relationships

### Inherits From
- [OSCollection](oscollection.md)
### Inherited By
- [OSSet](osset.md)

## See Also

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
- [OSCollection](oscollection.md)
  The base class for DriverKit collection objects.
- [OSContainer](oscontainer.md)
  The base class for DriverKit data objects.
- [OSObject](osobject.md)
  The base class for DriverKit objects
- [OSSymbol](ossymbol.md)
  A container for managing an array of characters.
- [IOFixed](iofixed.md)
  A fixed-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray)*