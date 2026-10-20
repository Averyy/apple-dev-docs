# getScaledValue

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a scaled version of the logical value.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual uint32_t getScaledValue(IOHIDValueScaleType type);
```

#### Return Value

Returns a scaled representation of the element value.

## Parameters

- `type`: The scale type to use. Scale types are defined by the IOHIDValueScaleType enumerator in - [`IOHIDValueScaleType`](../iohidvaluescaletype.md).

## See Also

### Accessing the Element’s Value
- [getValue](./getvalue.md)
  Gets the logical value that the device reported.
- [getDataValue](./getdatavalue.md)
  Gets the data value.
- [getScaledFixedValue](./getscaledfixedvalue.md)
  Returns a fixed number that represents the scaled version of the element’s logical value.
- [setValue](./setvalue.md)
  Sets the value of the element.
- [setDataValue](./setdatavalue.md)
  Sets the data value of the element.
- [getUnit](./getunit.md)
  Returns the units that you use to interpret the element’s value.
- [getUnitExponent](./getunitexponent.md)
  Returns the exponent that you use to interpret the element’s value.
- [IOHIDValueOptions](../iohidvalueoptions.md)
  A type for specifying value-related options.
- [Value Options](../value-options-enum.md)
  Options for how to retrieve an element’s values.
- [IOHIDValueScaleType](../iohidvaluescaletype.md)
  The type of scaling to use for an element’s value.
- [Value Scale Types](../value-scale-types-enum.md)
  The different types of scaling that you can perform on element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/getscaledvalue)*