# getValue

**Framework**: HIDDriverKit  
**Kind**: method

Gets the logical value that the device reported.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
uint32_t getValue(IOOptionBits options);
```

#### Return Value

Returns the element value.

## Parameters

- `options`: Optional options to pass in. Options are defined in the IOHIDValueOptions enumerator in  .

## See Also

- [getDataValue](iohidelement/getdatavalue.md)
  Gets the data value.
- [getScaledValue](iohidelement/getscaledvalue.md)
  Returns a scaled version of the logical value.
- [getScaledFixedValue](iohidelement/getscaledfixedvalue.md)
  Returns a fixed number that represents the scaled version of the element’s logical value.
- [setValue](iohidelement/setvalue.md)
  Sets the value of the element.
- [setDataValue](iohidelement/setdatavalue.md)
  Sets the data value of the element.
- [getUnit](iohidelement/getunit.md)
  Returns the units that you use to interpret the element’s value.
- [getUnitExponent](iohidelement/getunitexponent.md)
  Returns the exponent that you use to interpret the element’s value.
- [IOHIDValueOptions](iohidvalueoptions.md)
  A type for specifying value-related options.
- [Value Options](value-options-enum.md)
  Options for how to retrieve an element’s values.
- [IOHIDValueScaleType](iohidvaluescaletype.md)
  The type of scaling to use for an element’s value.
- [Value Scale Types](value-scale-types-enum.md)
  The different types of scaling that you can perform on element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/getvalue)*