# consumptionFormulaArguments

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The parameters the electric vehicle’s consumption model uses to calculate its energy consumption.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var consumptionFormulaArguments: [String : Any]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * consumptionFormulaArguments;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * consumptionFormulaArguments;
```

## Discussion

This property’s value is a dictionary of serializable objects that contains the parameters the electric vehicle’s consumption model uses to calculate its energy consumption as it travels. The keys of the dictionary must match those of the corresponding charging model. `model_id` is a mandatory key and must be the identifier of the consumption model the vehicle uses.

## See Also

### Providing Formula Arguments
- [var chargingFormulaArguments: [String : Any]?](./chargingformulaarguments.md)
  The parameters the electric vehicle’s charging model uses to calculate the duration of a charge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/consumptionformulaarguments)*