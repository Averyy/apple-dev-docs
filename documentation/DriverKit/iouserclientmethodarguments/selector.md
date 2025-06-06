# selector

**Framework**: DriverKit  
**Kind**: property

The index of the method you want to execute.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint64_t selector;
```

#### Discussion

When calling one of the IOKit connection methods, such as `IOConnectMethodScalarIScalarO`, the value in this property represents the index of the method you want to execute.

## See Also

- [version](iouserclientmethodarguments/version.md)
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
- [structureOutputMaximumSize](iouserclientmethodarguments/structureoutputmaximumsize.md)
  The maximum size of the output structure that you specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments/selector)*