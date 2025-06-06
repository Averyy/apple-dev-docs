# OSDictionary

**Framework**: DriverKit  
**Kind**: class

A container for a collection with elements that are key-value pairs.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSDictionary;
```

#### Overview

OSDictionary is a collection class for objects derived from OSObject. Storage and access are associative, based on keys that are uniqued OSObjects. OSString is commonly used as a key since it is uniqued. When adding an object to an OSDictionary, you provide a string identifier, which can then used to retrieve that object or remove it from the dictionary. Setting an object with a key that already has an associated object replaces the original object.

You must generally cast retrieved objects from OSObject to the desired class using the OSDynamicCast macro. This macro returns the object cast to the desired class, or `NULL` if the object isn’t derived from that class.

As with all DriverKit collection classes, OSDictionary retains objects added to it, and releases objects removed from it (or replaced). An OSDictionary also grows as necessary to accommodate new objects.

OSArray provides no concurrency protection; it’s up to the usage context to provide any protection necessary.

## Topics

### Creating a Dictionary
- [withCapacity](osdictionary/withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [withDictionary](osdictionary/withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [withObjects](osdictionary/withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [OSDictionaryCreate](osdictionarycreate.md)
- [merge](osdictionary/merge.md)
  Adds all members of a dictionary to this dictionary.
- [free](osdictionary/free.md)
- [flushCollection](osdictionary/flushcollection.md)
  Removes and drops references to all members of dictionary.
### Accessing Keys and Values
- [getObject](osdictionary/getobject-9ikoz.md)
  Returns a member of the dictionary.
- [getObject](osdictionary/getobject-8k3ie.md)
  Returns a member of the dictionary.
- [setObject](osdictionary/setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [setObject](osdictionary/setobject-7q0u2.md)
  Add or replace an object in the dictionary.
- [removeObject](osdictionary/removeobject-25qm5.md)
  Remove an object by key from the dictionary.
- [removeObject](osdictionary/removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [iterateObjects](osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [iterateObjects](osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](osdictionaryiterateobjectscallback.md)
### Getting and Setting Values
- [OSDictionaryGetValue](osdictionarygetvalue.md)
- [OSDictionaryGetStringValue](osdictionarygetstringvalue.md)
- [OSDictionaryGetUInt64Value](osdictionarygetuint64value.md)
- [OSDictionarySetValue](osdictionarysetvalue.md)
- [OSDictionarySetStringValue](osdictionarysetstringvalue.md)
- [OSDictionarySetUInt64Value](osdictionarysetuint64value.md)
- [OSDictionaryPtr](osdictionaryptr.md)
### Inspecting a Dictionary
- [ensureCapacity](osdictionary/ensurecapacity.md)
  Allocates capacity for members in dictionary.
- [getCapacity](osdictionary/getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [getCount](osdictionary/getcount.md)
  Returns count of members in dictionary.
- [OSDictionaryGetCount](osdictionarygetcount.md)
### Modifying the Dictionary Items
- [OSDictionaryApply](osdictionaryapply.md)
- [OSDictionaryApplier](osdictionaryapplier.md)
### Comparing Dictionaries
- [isEqualTo](osdictionary/isequalto-3c1k0.md)
  Compares all members of two dictionaries with isEqualTo().
- [isEqualTo](osdictionary/isequalto-2p9or.md)
  Compares certain members of two dictionaries with isEqualTo().
- [isEqualTo](osdictionary/isequalto-3kuk7.md)
  Compares the dictionary with an OSObject

## Relationships

### Inherits From
- [OSCollection](oscollection.md)

## See Also

- [OSArray](osarray.md)
  A container for an ordered, random-access collection of objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary)*