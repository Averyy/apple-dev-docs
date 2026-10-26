# setMaximumPower(_:for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Sets the maximum power for a specific type of charging connector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func setMaximumPower(_ power: Measurement<UnitPower>, for chargingConnectorType: INCar.ChargingConnectorType)
```

```objc
- (void) setMaximumPower:(NSMeasurement<NSUnitPower *> *) power forChargingConnectorType:(INCarChargingConnectorType) chargingConnectorType;
```

#### Discussion

Call this method for each type of charging connector the electric vehicle supports.

## Parameters

- `power`: The maximum power in watts that the charging connector supports.
- `chargingConnectorType`: The type of charging connector to update. See [`INCar.ChargingConnectorType`](./chargingconnectortype.md) for the types of charging connectors the system supports.

## See Also

### Providing a Charging Connector’s Maximum Power
- [func maximumPower(for: INCar.ChargingConnectorType) -> Measurement<UnitPower>?](./maximumpower%28for%29.md)
  Gets the maximum power for a specific type of charging connector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/setmaximumpower(_:for:))*