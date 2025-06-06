# AMError.Code.conversionNoDataError

**Framework**: Automator  
**Kind**: case

An error that occurs when the converter determines that the conversion, though possible, would produce a nil result.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case conversionNoDataError
```

#### Discussion

This error isn’t displayed to the user.

## See Also

- [AMError.Code.conversionFailedError](amerror/code/conversionfailederror.md)
  An error that occurs when, for example, the converter encounters an error converting data from one type to another.
- [AMError.Code.conversionNotPossibleError](amerror/code/conversionnotpossibleerror.md)
  An error that occurs when the converter determines that it is unable to convert from one data type to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/conversionnodataerror)*