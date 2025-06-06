# OSSet

**Framework**: DriverKit  
**Kind**: class

OSSet provides an unordered set store of objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSSet;
```

#### Overview

OSSet is a container for Libkern C++ objects (those derived from [`OSMetaClassBase`](osmetaclassbase.md), in particular [`OSObject`](osobject.md)). Storage and access follow basic set logic: you can add or remove an object, and test whether the set contains a particular object. A given object is only stored in the set once, and there is no ordering of objects in the set. A subclass [`OSOrderedSet`](osorderedset.md), provides for ordered set logic.

As with all Libkern collection classes, OSSet retains objects added to it, and releases objects removed from it. An OSSet also grows as necessary to accommodate new objects, unlike Core Foundation collections (it does not, however, shrink).

#### Use Restrictions

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are unsafe to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSet provides no concurrency protection; it’s up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as `IORegistryEntry`, handle synchronization via defined member functions for setting properties.

## Topics

### Instance Methods
- [containsObject](osset/containsobject.md)
- [getAnyObject](osset/getanyobject.md)
  Returns an arbitrary (not random) object from the set.
- [init](osset/init.md)
- [member](osset/member.md)
  Checks the set for the presence of an object.
- [merge](osset/merge.md)
  Adds the contents of an OSet to the set.
- [removeObject](osset/removeobject.md)
- [setObject](osset/setobject.md)
  Adds an object to the OSSet if it is not already present.
### Type Methods
- [withArray](osset/witharray.md)
  Creates and initializes an OSSet populated with the contents of an OSArray.
- [withCapacity](osset/withcapacity.md)
- [withObjects](osset/withobjects.md)
  Creates and initializes an OSSet populated with objects provided.

## Relationships

### Inherits From
- [OSArray](osarray.md)
### Inherited By
- [OSOrderedSet](osorderedset.md)

## See Also

- [IOCallOnceBlock](iocallonceblock.md)
- [IOCallOnceFlag](iocallonceflag.md)
- [IOCommand](iocommand.md)
- [IOCommandPool](iocommandpool.md)
- [IOCommandPoolPtr](iocommandpoolptr.md)
- [IOCommandPtr](iocommandptr.md)
- [IODMACommand](iodmacommand.md)
  An object that converts memory references to I/O bus addresses.
- [IODMACommandSpecification](iodmacommandspecification.md)
- [IODispatchAction](iodispatchaction.md)
- [IOHistogramReporter_IVars](iohistogramreporter_ivars.md)
- [IOReportLegendEntry](ioreportlegendentry.md)
- [IOReporter_IVars](ioreporter_ivars.md)
- [IOSimpleReporter_IVars](iosimplereporter_ivars.md)
- [IOStateReporter_IVars](iostatereporter_ivars.md)
- [IOStateReporter_valueSelector](iostatereporter_valueselector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset)*