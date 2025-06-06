# kIOHIDValueScaleTypeCalibrated

**Framework**: HIDDriverKit  
**Kind**: case

An option to scale the value with respect to a set of calibration properties.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOHIDValueScaleTypeCalibrated
```

#### Discussion

The system sets calibration properties for some types of data. For example, the built-in event driver calibrates digitizer data to the logical minimum and maximum values. If no calibration properties are set, the [`getScaledValue`](iohidelement/getscaledvalue.md) method calibrates the value to the range `-1` to `1`.

## See Also

- [kIOHIDValueScaleTypePhysical](kiohidvaluescaletypephysical.md)
  An option to scale the value with respect to the physical minimum and maximum values.
- [kIOHIDValueScaleTypeExponent](kiohidvaluescaletypeexponent.md)
  An option to scale the value with respect to the element’s unit exponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/kiohidvaluescaletypecalibrated)*