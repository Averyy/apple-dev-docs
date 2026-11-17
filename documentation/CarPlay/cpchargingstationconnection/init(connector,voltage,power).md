# init(connector:voltage:power:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a charging station connection object with information about a specific charging configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(connector: CPChargingStationConnection.Connector, voltage: Measurement<UnitElectricPotentialDifference>, power: Measurement<UnitPower>)
```

```objc
- (instancetype) initWithConnector:(CPChargingStationConnectionConnector) connector voltage:(NSMeasurement<NSUnitElectricPotentialDifference *> *) voltage power:(NSMeasurement<NSUnitPower *> *) power;
```

## Return Value

An initialized charging station connection object.

## Discussion

Create one or more `CPChargingStationConnection` objects to represent the primary configurations available at the charging station.

## Parameters

- `connector`: The type of connector available at the charging station.
- `voltage`: The voltage the connector supplies to the vehicle.
- `power`: The amount of power the plug delivers to the vehicle.

## See Also

### Creating a charging station connection
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/init(connector:voltage:power:))*