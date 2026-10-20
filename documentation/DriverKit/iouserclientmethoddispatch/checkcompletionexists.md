# checkCompletionExists

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

An integer value indicating whether to check for the existence of a completion action.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint32_t checkCompletionExists;
```

#### Discussion

If the value of this field is a positive unsigned integer, the [`completion`](../iouserclientmethodarguments/completion.md) field must be set to a valid action. If the value is `0`, the [`completion`](../iouserclientmethodarguments/completion.md) field must be `NULL`. If the value of this field is -1U, the [`completion`](../iouserclientmethodarguments/completion.md) field is ignored.

## See Also

### Getting the Dispatch Properties
- [function](./function.md)
  The function to call after validating all of the specified values.
- [checkScalarInputCount](./checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](./checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](./checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](./checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkcompletionexists)*