# function

**Framework**: DriverKit  
**Kind**: property

The function to call after validating all of the specified values.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOUserClientMethodFunction function;
```

#### Discussion

If this property is `NULL` and all checks pass, the system returns `kIOReturnNoCompletion` for the caller to implement the method.

## See Also

- [checkCompletionExists](iouserclientmethoddispatch/checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkScalarInputCount](iouserclientmethoddispatch/checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](iouserclientmethoddispatch/checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](iouserclientmethoddispatch/checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](iouserclientmethoddispatch/checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/function)*