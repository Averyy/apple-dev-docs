# connector

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The type of connector the station provides for vehicles.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var connector: CPChargingStationConnection.Connector { get }
```

```objc
@property (nonatomic, assign, readonly) CPChargingStationConnectionConnector connector;
```

## See Also

### Getting the connector information
- [var voltage: Measurement<UnitElectricPotentialDifference>](./voltage.md)
  The supported voltage level at the charging station.
- [var power: Measurement<UnitPower>](./power.md)
  The supported power level at the charging station.
- [CPChargingStationConnection.Connector](./connector-swift.enum.md)
  Constants for the connector types available at charging stations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/connector-swift.property)*