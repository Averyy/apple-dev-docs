# OSString

**Framework**: DriverKit  
**Kind**: class

A container for managing an array of characters.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSString;
```

#### Overview

OSString is a container class for managing arrays of characters.

OSString makes no provisions for different character encodings and assumes that a string is a nul-terminated sequence of single-byte characters. User-space code must either assume an encoding (typically ASCII or UTF-8) or determine it in some other way (such as an IORegistryEntry property).

OSString is immutable.

## Topics

### Creating a String
- [withString](osstring/withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [withCString](osstring/withcstring-4wsql.md)
  Allocates an OSString object with a copy of a c-string.
- [withCString](osstring/withcstring-721oh.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [withCStringNoCopy](osstring/withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [OSStringCreate](osstringcreate.md)
- [free](osstring/free.md)
### Getting a C String
- [getCStringNoCopy](osstring/getcstringnocopy.md)
  Returns a pointer to the OSString object’s internal data buffer.
- [OSStringGetStringPtr](osstringgetstringptr.md)
- [OSStringPtr](osstringptr.md)
### Inspecting a String
- [getLength](osstring/getlength.md)
  Returns length of string not including null terminator.
- [OSStringGetLength](osstringgetlength.md)
### Comparing Strings
- [isEqualTo](osstring/isequalto-1uq1f.md)
  Compares the string with an OSData.
- [isEqualTo](osstring/isequalto-712xj.md)
  Compares the string with an OSObject
- [isEqualTo](osstring/isequalto-5paj5.md)
  Compares the string with an OSString.
- [isEqualTo](osstring/isequalto-2rg80.md)
  Compares the string with a c-string.

## Relationships

### Inherits From
- [OSContainer](oscontainer.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring)*