# structureOutputMaximumSize

**Framework**: DriverKit  
**Kind**: property

The maximum size of the output structure that you specified.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint64_t structureOutputMaximumSize;
```

#### Discussion

Specify [`kIOUserClientVariableStructureSize`](kiouserclientvariablestructuresize.md) to allow for output data that is variable in size.

## See Also

- [version](iouserclientmethodarguments/version.md)
- [selector](iouserclientmethodarguments/selector.md)
  The index of the method you want to execute.
- [completion](iouserclientmethodarguments/completion.md)
  An action for processing asynchronous data received from the service.
- [scalarInput](iouserclientmethodarguments/scalarinput.md)
  An array of scalars from the caller.
- [scalarInputCount](iouserclientmethodarguments/scalarinputcount.md)
  The number of scalars provided by the caller.
- [structureInput](iouserclientmethodarguments/structureinput.md)
  A data object containing the structure input from the IOKit connect method.
- [structureInputDescriptor](iouserclientmethodarguments/structureinputdescriptor.md)
  A memory descriptor containing structure input from the IOKit connect method.
- [scalarOutput](iouserclientmethodarguments/scalaroutput.md)
  An array of scalars to return to the caller.
- [scalarOutputCount](iouserclientmethodarguments/scalaroutputcount.md)
  The number of scalars to return to the caller.
- [structureOutput](iouserclientmethodarguments/structureoutput.md)
  A data object to return to the caller as structure output.
- [structureOutputDescriptor](iouserclientmethodarguments/structureoutputdescriptor.md)
  An IOMemoryDescriptor specified by the caller for structure output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments/structureoutputmaximumsize)*