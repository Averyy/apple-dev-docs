# checkStructureInputSize

**Framework**: DriverKit  
**Kind**: property

The expected size of the scalar inputs.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint32_t checkStructureInputSize;
```

#### Discussion

If the value of this field is [`kIOUserClientVariableStructureSize`](kiouserclientvariablestructuresize.md), don’t validate the structure size. For all other values, the value in this property must equal the value in either the [`structureInput`](iouserclientmethodarguments/structureinput.md) or [`structureInputDescriptor`](iouserclientmethodarguments/structureinputdescriptor.md) fields of the [`IOUserClientMethodArguments`](iouserclientmethodarguments.md) structure.

## See Also

- [function](iouserclientmethoddispatch/function.md)
  The function to call after validating all of the specified values.
- [checkCompletionExists](iouserclientmethoddispatch/checkcompletionexists.md)
  An integer value indicating whether to check for the existence of a completion action.
- [checkScalarInputCount](iouserclientmethoddispatch/checkscalarinputcount.md)
  The expected number of scalar inputs.
- [checkScalarOutputCount](iouserclientmethoddispatch/checkscalaroutputcount.md)
  The expected number of scalar outputs.
- [checkStructureOutputSize](iouserclientmethoddispatch/checkstructureoutputsize.md)
  The expected size of the scalar outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethoddispatch/checkstructureinputsize)*