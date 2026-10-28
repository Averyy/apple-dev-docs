# structureInputDescriptor

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

A memory descriptor containing structure input from the IOKit connect method.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
IOMemoryDescriptor * structureInputDescriptor;
```

## Discussion

This parameter is set only for large structures, and if set [`structureInput`](./structureinput.md) is `NULL`.

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
- [scalarOutput](./scalaroutput.md)
  An array of scalars to return to the caller.
- [scalarOutputCount](./scalaroutputcount.md)
  The number of scalars to return to the caller.
- [structureOutput](./structureoutput.md)
  A data object to return to the caller as structure output.
- [structureOutputDescriptor](./structureoutputdescriptor.md)
  An IOMemoryDescriptor specified by the caller for structure output.
- [structureOutputMaximumSize](./structureoutputmaximumsize.md)
  The maximum size of the output structure that you specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments/structureinputdescriptor)*