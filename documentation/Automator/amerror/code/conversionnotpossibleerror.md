# AMError.Code.conversionNotPossibleError

**Framework**: Automator  
**Kind**: case  
**Role**: Case

An error that occurs when the converter determines that it is unable to convert from one data type to another.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case conversionNotPossibleError
```

```c
AMConversionNotPossibleError
```

#### Discussion

This error isn’t displayed to the user.

## See Also

### Data Conversion Errors
- [AMError.Code.conversionFailedError](./conversionfailederror.md)
  An error that occurs when, for example, the converter encounters an error converting data from one type to another.
- [AMError.Code.conversionNoDataError](./conversionnodataerror.md)
  An error that occurs when the converter determines that the conversion, though possible, would produce a nil result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/conversionnotpossibleerror)*