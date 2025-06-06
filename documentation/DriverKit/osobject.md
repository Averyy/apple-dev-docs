# OSObject

**Framework**: DriverKit  
**Kind**: class

The base class for DriverKit objects

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSObject;
```

## Topics

### Managing the Object Lifecycle
- [init](osobject/init.md)
- [retain](osobject/retain.md)
  Retains the OSObject instance
- [release](osobject/release.md)
  Releases the OSObject instance
- [free](osobject/free.md)
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
### Managing an Object’s Dispatch Queue
- [SetDispatchQueue](osobject/setdispatchqueue.md)
- [CopyDispatchQueue](osobject/copydispatchqueue.md)

## Relationships

### Inherits From
- [OSMetaClassBase](osmetaclassbase.md)
### Inherited By
- [IOCommand](iocommand.md)
- [IOCommandPool](iocommandpool.md)
- [IODMACommand](iodmacommand.md)
- [IODispatchQueue](iodispatchqueue.md)
- [IODispatchSource](iodispatchsource.md)
- [IOMemoryDescriptor](iomemorydescriptor.md)
- [IOMemoryMap](iomemorymap.md)
- [IOReportLegend](ioreportlegend.md)
- [IOReporter](ioreporter.md)
- [IOService](ioservice.md)
- [OSAction](osaction.md)
- [OSBundle](osbundle.md)
- [OSContainer](oscontainer.md)
- [OSMappedFile](osmappedfile.md)

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
- [OSCollection](oscollection.md)
  The base class for DriverKit collection objects.
- [OSContainer](oscontainer.md)
  The base class for DriverKit data objects.
- [OSSymbol](ossymbol.md)
  A container for managing an array of characters.
- [IOFixed](iofixed.md)
  A fixed-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobject)*