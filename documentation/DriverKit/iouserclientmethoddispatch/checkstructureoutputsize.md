# checkStructureOutputSize

**Framework**: DriverKit  
**Kind**: property  
**Role**: Instance Property

The expected size of the scalar outputs.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
uint32_t checkStructureOutputSize;
```

#### Discussion

If the value of this field is [`kIOUserClientVariableStructureSize`](../kiouserclientvariablestructuresize.md), don’t validate the structure size. For all other values, the value in this property must equal the value in the [`structureOutputMaximumSize`](../iouserclientmethodarguments/structureoutputmaximumsize.md) field of the [`IOUserClientMethodArguments`](../iouserclientmethodarguments.md) structure.

## See Also

### Getting the Dispatch Properties
- [function](./function.md)
  The function to call after validating all of the specified values.
- [checkCompletionExists](./checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkScalarInputCount](./checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](./checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkScalarOutputCount](./checkscalaroutputcount.md)
  The expected number of scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkstructureoutputsize)*