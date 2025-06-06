# checkCompletionExists

**Framework**: DriverKit  
**Kind**: property

An integer value indicating whether to check for the existence of a completion action.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint32_t checkCompletionExists;
```

#### Discussion

If the value of this field is a positive unsigned integer, the [`completion`](iouserclientmethodarguments/completion.md) field must be set to a valid action. If the value is `0`, the [`completion`](iouserclientmethodarguments/completion.md) field must be `NULL`. If the value of this field is -1U, the [`completion`](iouserclientmethodarguments/completion.md) field is ignored.

## See Also

- [function](iouserclientmethoddispatch/function.md)
  The function to call after validating all of the specified values.
- [checkScalarInputCount](iouserclientmethoddispatch/checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](iouserclientmethoddispatch/checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](iouserclientmethoddispatch/checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](iouserclientmethoddispatch/checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkcompletionexists)*