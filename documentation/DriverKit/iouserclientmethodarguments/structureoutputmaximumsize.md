# structureOutputMaximumSize

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

The maximum size of the output structure that you specified.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint64_t structureOutputMaximumSize;
```

#### Discussion

Specify [`kIOUserClientVariableStructureSize`](../kiouserclientvariablestructuresize.md) to allow for output data that is variable in size.

## See Also

### Getting the Method Arguments
- [version](./version.md)
- [selector](./selector.md)
  The index of the method you want to execute.
- [completion](./completion.md)
  An action for processing asynchronous data received from the service.
- [scalarInput](./scalarinput.md)
  An array of scalars from the caller.
- [scalarInputCount](./scalarinputcount.md)
  The number of scalars provided by the caller.
- [structureInput](./structureinput.md)
  A data object containing the structure input from the IOKit connect method.
- [structureInputDescriptor](./structureinputdescriptor.md)
  A memory descriptor containing structure input from the IOKit connect method.
- [scalarOutput](./scalaroutput.md)
  An array of scalars to return to the caller.
- [scalarOutputCount](./scalaroutputcount.md)
  The number of scalars to return to the caller.
- [structureOutput](./structureoutput.md)
  A data object to return to the caller as structure output.
- [structureOutputDescriptor](./structureoutputdescriptor.md)
  An IOMemoryDescriptor specified by the caller for structure output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments/structureoutputmaximumsize)*