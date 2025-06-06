# IOCommand

**Framework**: DriverKit  
**Kind**: class

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOCommand;
```

#### Overview

This class is an abstract class which represents an I/O command.

This class is an abstract class which represents an I/O command passed from a device driver to a controller. All controller commands (e.g. IOATACommand) should inherit from this class.

## Topics

### Instance Methods
- [CommandChain](iocommand/commandchain.md)
- [free](iocommand/free.md)
- [init](iocommand/init.md)
### Type Methods
- [FromChain](iocommand/fromchain.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOCallOnceBlock](iocallonceblock.md)
- [IOCallOnceFlag](iocallonceflag.md)
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
- [IVarsInvalidator](ivarsinvalidator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommand)*