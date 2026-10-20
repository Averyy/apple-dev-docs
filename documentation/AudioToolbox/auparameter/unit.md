# unit

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The parameter’s unit of measurement.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var unit: AudioUnitParameterUnit { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) AudioUnitParameterUnit unit;
```

*macOS*

```objc
@property (atomic, readonly) AudioUnitParameterUnit unit;
```

## See Also

### Querying Parameter Properties
- [var minValue: AUValue](./minvalue.md)
  The parameter’s minimum value.
- [var maxValue: AUValue](./maxvalue.md)
  The parameter’s maximum value.
- [var unitName: String?](./unitname.md)
  The parameter’s localized unit name.
- [var flags: AudioUnitParameterOptions](./flags.md)
  The parameter’s characteristic details.
- [var address: AUParameterAddress](./address.md)
  The parameter’s address.
- [var valueStrings: [String]?](./valuestrings.md)
  The parameter’s localized value strings.
- [var dependentParameters: [NSNumber]?](./dependentparameters.md)
  Any other parameter’s whose values may change as a side effect of this parameter’s value changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/unit)*