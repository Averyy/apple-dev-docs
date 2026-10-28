# checkScalarInputCount

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

The expected number of scalar inputs.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint32_t checkScalarInputCount;
```

## Discussion

If the value of this field is [`kIOUserClientVariableStructureSize`](../kiouserclientvariablestructuresize.md), ignore the value of the [`scalarInputCount`](../iouserclientmethodarguments/scalarinputcount.md) field. For all other values, the value in this property must equal the value in the [`scalarInputCount`](../iouserclientmethodarguments/scalarinputcount.md) field of the [`IOUserClientMethodArguments`](../iouserclientmethodarguments.md) structure.

## See Also

### Getting the Dispatch Properties
- [function](./function.md)
  The function to call after validating all of the specified values.
- [checkCompletionExists](./checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkStructureInputSize](./checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](./checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](./checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkscalarinputcount)*