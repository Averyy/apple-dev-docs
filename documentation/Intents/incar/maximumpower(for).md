# maximumPower(for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Gets the maximum power for a specific type of charging connector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func maximumPower(for chargingConnectorType: INCar.ChargingConnectorType) -> Measurement<UnitPower>?
```

```objc
- (NSMeasurement<NSUnitPower *> *) maximumPowerForChargingConnectorType:(INCarChargingConnectorType) chargingConnectorType;
```

#### Return Value

The maximum power in watts for the charging connector, or `nil` if you haven’t set a value using [`setMaximumPower(_:for:)`](./setmaximumpower%28_,for%29.md).

## Parameters

- `chargingConnectorType`: The type of charging connector to query for its maximum power. See [`INCar.ChargingConnectorType`](./chargingconnectortype.md) for the types of charging connectors the system supports.

## See Also

### Providing a Charging Connector’s Maximum Power
- [func setMaximumPower(Measurement<UnitPower>, for: INCar.ChargingConnectorType)](./setmaximumpower%28_,for%29.md)
  Sets the maximum power for a specific type of charging connector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/maximumpower(for:))*