# Value Scale Types

**Framework**: HIDDriverKit

The different types of scaling that you can perform on element values.

## Topics

### Getting the Options
- [kIOHIDValueScaleTypeCalibrated](kiohidvaluescaletypecalibrated.md)
  An option to scale the value with respect to a set of calibration properties.
- [kIOHIDValueScaleTypePhysical](kiohidvaluescaletypephysical.md)
  An option to scale the value with respect to the physical minimum and maximum values.
- [kIOHIDValueScaleTypeExponent](kiohidvaluescaletypeexponent.md)
  An option to scale the value with respect to the element’s unit exponent.

## See Also

- [getValue](iohidelement/getvalue.md)
  Gets the logical value that the device reported.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/value-scale-types-enum)*