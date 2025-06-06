# OSData

**Framework**: DriverKit  
**Kind**: class

A container for untyped data.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSData;
```

#### Overview

OSData represents an array of bytes as a container object. OSData objects are mutable: You can add bytes to them and overwrite portions of the byte array.

OSData provides no concurrency protection; it’s up to the usage context to provide any protection necessary.

## Topics

### Creating a Data Object
- [withBytes](osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [withBytesNoCopy](osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [withCapacity](osdata/withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [withData](osdata/withdata-9y3g.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [withData](osdata/withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataCreate](osdatacreate.md)
- [OSDataPtr](osdataptr.md)
- [free](osdata/free.md)
### Getting Bytes
- [getBytesNoCopy](osdata/getbytesnocopy-91vcg.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [getBytesNoCopy](osdata/getbytesnocopy-53puz.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [OSDataGetBytes](osdatagetbytes.md)
- [OSDataGetBytesPtr](osdatagetbytesptr.md)
### Appending Data to the Object
- [appendBytes](osdata/appendbytes-lbqa.md)
  Appends a buffer of bytes to the OSData object’s internal data buffer.
- [appendBytes](osdata/appendbytes-38hs5.md)
  Appends a buffer of bytes to the OSData object’s internal data buffer.
- [appendBytes](osdata/appendbytes-lbqa.md)
  Appends a buffer of bytes to the OSData object’s internal data buffer.
- [OSDataAppendBytes](osdataappendbytes.md)
### Inspecting a Data Object
- [getCapacity](osdata/getcapacity.md)
  Returns length of preallocated capacity.
- [getLength](osdata/getlength.md)
  Returns length of data present.
- [OSDataGetLength](osdatagetlength.md)
### Comparing Data Objects
- [isEqualTo](osdata/isequalto-2kdml.md)
  Compares the data with an OSData
- [isEqualTo](osdata/isequalto-4xz0j.md)
  Compares the data with an OSObject
- [isEqualTo](osdata/isequalto-5ssf5.md)
  Compares the data with an OSString
- [isEqualTo](osdata/isequalto-79gqy.md)
  Compares the data with a pointer to bytes

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata)*