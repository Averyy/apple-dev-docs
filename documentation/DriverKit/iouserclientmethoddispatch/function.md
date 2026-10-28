# function

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

The function to call after validating all of the specified values.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
IOUserClientMethodFunction function;
```

## Discussion

If this property is `NULL` and all checks pass, the system returns `kIOReturnNoCompletion` for the caller to implement the method.

## See Also

### Getting the Dispatch Properties
- [checkCompletionExists](./checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkScalarInputCount](./checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](./checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](./checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](./checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/function)*