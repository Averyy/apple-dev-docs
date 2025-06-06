# OSSerialization

**Framework**: DriverKit  
**Kind**: class

A container for one or more objects, serialized in a binary data format that is suitable for messaging.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSSerialization;
```

#### Overview

OSSerialization provides methods to serialize an object to binary data suitable for messaging. Only certain DriverKit classes may be serialized: OSData, OSString, OSNumber, OSBoolean, OSArray, OSDictionary.

OSSerialization provides no concurrency protection; it’s up to the usage context to provide any protection necessary.

## Topics

### Creating a Serialization Object
- [createFromBytes](osserialization/createfrombytes.md)
  Allocates an OSSerialization object from the serialized data of a previous serialization.
- [createFromObject](osserialization/createfromobject.md)
  Allocates an OSSerialization object with the serialized data of an object.
- [OSCreateSerializationFromBytes](oscreateserializationfrombytes.md)
- [OSCreateSerializationFromObject](oscreateserializationfromobject.md)
- [free](osserialization/free.md)
- [OSSerializationFreeBufferHandler](osserializationfreebufferhandler.md)
- [OSSerializationPtr](osserializationptr.md)
### Getting the Serialized Content
- [copyObject](osserialization/copyobject.md)
  Obtain the result of the deserialization performed by createFromBytes().
- [OSCreateObjectFromSerialization](oscreateobjectfromserialization.md)
- [OSSerializationGetBytes](osserializationgetbytes.md)
- [finalizeBuffer](osserialization/finalizebuffer.md)
  Obtain the result of the serialization performed by createFromObject().
### Type Methods
- [freeBuffer](osserialization/freebuffer.md)

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
- [OSString](osstring.md)
  A container for managing an array of characters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization)*