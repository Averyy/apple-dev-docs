# checkScalarOutputCount

**Framework**: DriverKit  
**Kind**: property

The expected number of scalar outputs.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint32_t checkScalarOutputCount;
```

#### Discussion

If the value of this field is [`kIOUserClientVariableStructureSize`](kiouserclientvariablestructuresize.md), ignore the value of the [`scalarOutputCount`](iouserclientmethodarguments/scalaroutputcount.md) field. For all other values, the value in this property must equal the value in the [`scalarOutputCount`](iouserclientmethodarguments/scalaroutputcount.md) field of the [`IOUserClientMethodArguments`](iouserclientmethodarguments.md) structure.

## See Also

- [function](iouserclientmethoddispatch/function.md)
  The function to call after validating all of the specified values.
- [checkCompletionExists](iouserclientmethoddispatch/checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkScalarInputCount](iouserclientmethoddispatch/checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkStructureInputSize](iouserclientmethoddispatch/checkstructureinputsize.md)
  The expected size of the scalar inputs.
- [checkStructureOutputSize](iouserclientmethoddispatch/checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkscalaroutputcount)*