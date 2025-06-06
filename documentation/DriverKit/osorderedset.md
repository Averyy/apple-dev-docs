# OSOrderedSet

**Framework**: DriverKit  
**Kind**: class

OSOrderedSet provides an ordered set store of objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSOrderedSet;
```

#### Overview

[`OSOrderedSet`](osorderedset.md) is a container for Libkern C++ objects (those derived from [`OSMetaClassBase`](osmetaclassbase.md), in particular OSObject). Storage and access follow ordered set logic. A given object is stored in the set only once, but you can:

- Define a sorting function for automated ordering (upon addition only)
- Manually insert new objects in the set (overriding sorting)
- Add and remove objects in the set
- Test whether the set contains a particular object
- Get the object stored at a particular index.

Note that automated ordering is performed only upon addition of objects and depends on the existing objects being properly sorted. There is no function to re-sort the contents of an OSOrderedSet or to change the ordering function. In general, you should either use the one ordered-insertion function, or the indexed-insertion functions, and not mix the two.

As with all Libkern collection classes, [`OSOrderedSet`](osorderedset.md) retains objects added to it, and releases objects removed from it. An [`OSOrderedSet`](osorderedset.md) also grows as necessary to accommodate new objects, unlike Core Foundation collections (it does not, however, shrink).

#### Use Restrictions

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are unsafe to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSOrderedSet provides no concurrency protection; it’s up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as `IORegistryEntry`, handle synchronization via defined member functions for setting properties.

## Topics

### Instance Methods
- [free](osorderedset/free.md)
- [getFirstObject](osorderedset/getfirstobject.md)
  The object at index 0 in the ordered set if there is one, otherwise `NULL`.
- [getLastObject](osorderedset/getlastobject.md)
  The last object in the ordered set if there is one, otherwise `NULL`.
- [init](osorderedset/init.md)
- [orderObject](osorderedset/orderobject.md)
  Calls the ordered set’s order function against a `NULL` object.
- [setFirstObject](osorderedset/setfirstobject.md)
  Adds an object to the OSOrderedSet at index 0 if it is not already present.
- [setLastObject](osorderedset/setlastobject.md)
  Adds an object at the end of the OSOrderedSet if it is not already present.
- [setObject](osorderedset/setobject.md)
  Adds an object to the OSOrderedSet if it is not already present, storing it in sorted order if there is an order function.
### Type Methods
- [withCapacity](osorderedset/withcapacity.md)

## Relationships

### Inherits From
- [OSSet](osset.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osorderedset)*