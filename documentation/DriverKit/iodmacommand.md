# IODMACommand

**Framework**: DriverKit  
**Kind**: class

An object that converts memory references to I/O bus addresses.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IODMACommand;
```

#### Overview

The [`IODMACommand`](iodmacommand.md) class supersedes [`IOMemoryCursor`](https://developer.apple.com/documentation/kernel/iomemorycursor) and greatly enhances the functionality and power of it. The command can be specified to output 64 bit physical addresses and also allows driver writers to bypass mapping hardware or get addresses suitable for non-snooped DMA.

The command is designed to be very easily subclassable. Most driver writers need to associate some DMA operations with their memory descriptor, and usually use a C structure for that purpose. This structure is often kept in a linked list. This [`IODMACommand`](iodmacommand.md) has built-in `<kern/queue.h>` linkage and can be derived and ‘public:’ variables added, giving the developer a structure that can associate a memory descriptor with a particular DMA command but will also allow the developer to generate that command and keep the state necessary for tracking it.

Create a pool of [`IODMACommand`](iodmacommand.md) objects at driver initialization, and keep each command in an [`IOCommandPool`](iocommandpool.md) when not in use. You may also maintain your own free list of objects if preferred. See the `<kern/queue.h>` and `<xnu/iokit/Kernel/IOCommandPool>` for sample code on manipulating the command’s doubly linked list entries.

You can use an [`IODMACommand`](iodmacommand.md) object in a ‘weak-linked’ manner. To do this you must avoid using any static member functions. Use the much slower, but safe, [`weakWithSpecification`](https://developer.apple.com/documentation/kernel/1547721-weakwithspecification) function. On success, the function returns a DMA command object, which you can use to clone as many commands as needed.

## Topics

### Creating a DMA Command
- [init](iodmacommand/init.md)
- [free](iodmacommand/free.md)
- [Create](iodmacommand/create.md)
### Performing Internal Operations
- [CompleteDMA](iodmacommand/completedma.md)
- [GetPreparation](iodmacommand/getpreparation.md)
- [PerformOperation](iodmacommand/performoperation.md)
- [PrepareForDMA](iodmacommand/preparefordma.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOCallOnceBlock](iocallonceblock.md)
- [IOCallOnceFlag](iocallonceflag.md)
- [IOCommand](iocommand.md)
- [IOCommandPool](iocommandpool.md)
- [IOCommandPoolPtr](iocommandpoolptr.md)
- [IOCommandPtr](iocommandptr.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand)*