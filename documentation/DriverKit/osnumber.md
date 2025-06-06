# OSNumber

**Framework**: DriverKit  
**Kind**: class

A container for an integer value.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSNumber;
```

#### Overview

OSNumber represents an integer of 8, 16, 32, or 64 bits as a DriverKit container object. OSNumber objects are immutable.

## Topics

### Creating a Number Object
- [withNumber](osnumber/withnumber-5rcqv.md)
  Allocates an OSNumber object with value and size.
- [withNumber](osnumber/withnumber-2c6oe.md)
  Allocates an OSNumber object with value from a c-string and size.
- [OSNumberCreateWithUInt64Value](osnumbercreatewithuint64value.md)
- [free](osnumber/free.md)
- [OSNumberPtr](osnumberptr.md)
### Getting Integer Values
- [unsigned8BitValue](osnumber/unsigned8bitvalue.md)
  Returns the value of the OSNumber as a uint8_t value.
- [unsigned16BitValue](osnumber/unsigned16bitvalue.md)
  Returns the value of the OSNumber as a uint16_t value.
- [unsigned32BitValue](osnumber/unsigned32bitvalue.md)
  Returns the value of the OSNumber as a uint32_t value.
- [unsigned64BitValue](osnumber/unsigned64bitvalue.md)
  Returns the value of the OSNumber as a uint64_t value.
- [OSNumberGetUInt64Value](osnumbergetuint64value.md)
### Inspecting a Number
- [numberOfBits](osnumber/numberofbits.md)
  Returns the number of bits the OSNumber was created with.
### Comparing Numbers
- [isEqualTo](osnumber/isequalto-333kh.md)
  Compares the string with an OSObject
- [isEqualTo](osnumber/isequalto-58rb9.md)
  Compares the number with an OSNumber.

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osnumber)*