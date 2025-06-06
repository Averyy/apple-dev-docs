# valueStrings

**Framework**: Audio Toolbox  
**Kind**: property

The parameter’s localized value strings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var valueStrings: [String]? { get }
```

#### Discussion

This property allows you to specify an array of strings to be used for the values of an indexed parameter—for example, a  parameter could publish these values: “High”, “Medium”, “Low”.

## See Also

- [var minValue: AUValue](auparameter/minvalue.md)
  The parameter’s minimum value.
- [var maxValue: AUValue](auparameter/maxvalue.md)
  The parameter’s maximum value.
- [var unit: AudioUnitParameterUnit](auparameter/unit.md)
  The parameter’s unit of measurement.
- [var unitName: String?](auparameter/unitname.md)
  The parameter’s localized unit name.
- [var flags: AudioUnitParameterOptions](auparameter/flags.md)
  The parameter’s characteristic details.
- [var address: AUParameterAddress](auparameter/address.md)
  The parameter’s address.
- [var dependentParameters: [NSNumber]?](auparameter/dependentparameters.md)
  Any other parameter’s whose values may change as a side effect of this parameter’s value changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/valuestrings)*