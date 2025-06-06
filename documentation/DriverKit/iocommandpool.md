# IOCommandPool

**Framework**: DriverKit  
**Kind**: class

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOCommandPool;
```

#### Overview

The IOCommandPool class is used to manipulate a pool of commands which inherit from IOCommand. The caller must put commands in the pool by creating the command (via the controller’s factory method or a memory allocation) and calling the returnCommand method with the newly created command as its argument.

## Topics

### Instance Methods
- [free](iocommandpool/free.md)
- [gatedGetCommand](iocommandpool/gatedgetcommand.md)
- [gatedReturnCommand](iocommandpool/gatedreturncommand.md)
- [getCommand](iocommandpool/getcommand.md)
- [init](iocommandpool/init.md)
- [initWithQueue](iocommandpool/initwithqueue.md)
- [returnCommand](iocommandpool/returncommand.md)
### Type Methods
- [withQueue](iocommandpool/withqueue.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOCallOnceBlock](iocallonceblock.md)
- [IOCallOnceFlag](iocallonceflag.md)
- [IOCommand](iocommand.md)
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
- [IVarsInvalidator](ivarsinvalidator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool)*