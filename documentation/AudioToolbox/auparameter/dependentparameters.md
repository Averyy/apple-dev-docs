# dependentParameters

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Any other parameter’s whose values may change as a side effect of this parameter’s value changing.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dependentParameters: [NSNumber]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * dependentParameters;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSNumber *> * dependentParameters;
```

#### Discussion

The array contains [`NSNumber`](../../Foundation/nsnumber.md) objects representing [`AUParameterAddress`](../auparameteraddress.md) values.

## See Also

### Querying Parameter Properties
- [var minValue: AUValue](./minvalue.md)
  The parameter’s minimum value.
- [var maxValue: AUValue](./maxvalue.md)
  The parameter’s maximum value.
- [var unit: AudioUnitParameterUnit](./unit.md)
  The parameter’s unit of measurement.
- [var unitName: String?](./unitname.md)
  The parameter’s localized unit name.
- [var flags: AudioUnitParameterOptions](./flags.md)
  The parameter’s characteristic details.
- [var address: AUParameterAddress](./address.md)
  The parameter’s address.
- [var valueStrings: [String]?](./valuestrings.md)
  The parameter’s localized value strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/dependentparameters)*