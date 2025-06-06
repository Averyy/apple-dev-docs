# IOUserClientMethodArguments

**Framework**: DriverKit  
**Kind**: struct

Arguments to pass to IOConnectMethod calls.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
struct IOUserClientMethodArguments;
```

#### Discussion

Any argument may be passed as NULL if not passed by the caller.

## Topics

### Getting the Method Arguments
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
- [structureOutputMaximumSize](iouserclientmethodarguments/structureoutputmaximumsize.md)
  The maximum size of the output structure that you specified.
### Getting Type Information
- [IOUserClientScalarArray](iouserclientscalararray.md)
- [Scalar Array Sizes](3325605-scalar_array_sizes.md)
- [Output Maximum Size](3325606-output_maximum_size.md)
  Constant to denote a variable length structure argument to IOUserClient.
- [Version Information](3325604-version_information.md)

## See Also

- [ExternalMethod](iouserclient/externalmethod.md)
  Receive arguments from IOKit.framework IOConnectMethod calls.
- [IOUserClientMethodDispatch](iouserclientmethoddispatch.md)
  A structure that specifies how to validate the arguments passed to a client method function.
- [IOUserClientMethodFunction](iouserclientmethodfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodarguments)*