# init(connector:voltage:power:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/init(connector:voltage:power:))*