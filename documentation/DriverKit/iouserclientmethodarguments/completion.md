# completion

**Framework**: DriverKit  
**Kind**: property

An action for processing asynchronous data received from the service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSAction * completion;
```

#### Discussion

The system retains this method only during the invocation of [`ExternalMethod`](iouserclient/externalmethod.md). Retain this method yourself if you intend to use it outside of that invocation.

## See Also

- [version](iouserclientmethodarguments/version.md)
- [selector](iouserclientmethodarguments/selector.md)
  The index of the method you want to execute.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments/completion)*