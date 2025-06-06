# minValue

**Framework**: Audio Toolbox  
**Kind**: property

The parameter’s minimum value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var minValue: AUValue { get }
```

## See Also

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
- [var valueStrings: [String]?](auparameter/valuestrings.md)
  The parameter’s localized value strings.
- [var dependentParameters: [NSNumber]?](auparameter/dependentparameters.md)
  Any other parameter’s whose values may change as a side effect of this parameter’s value changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/minvalue)*