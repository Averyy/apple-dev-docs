# voltage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The supported voltage level at the charging station.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var voltage: Measurement<UnitElectricPotentialDifference> { get }
```

```objc
@property (nonatomic, strong, readonly) NSMeasurement<NSUnitElectricPotentialDifference *> * voltage;
```

## Discussion

Voltage levels determine whether the station supports fast charging of vehicles. For example, a station that supports 240 volts or higher allows someone to charge their vehicle more quickly.

## See Also

### Getting the connector information
- [var connector: CPChargingStationConnection.Connector](./connector-swift.property.md)
  The type of connector the station provides for vehicles.
- [var power: Measurement<UnitPower>](./power.md)
  The supported power level at the charging station.
- [CPChargingStationConnection.Connector](./connector-swift.enum.md)
  Constants for the connector types available at charging stations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/voltage)*