# power

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The supported power level at the charging station.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var power: Measurement<UnitPower> { get }
```

```objc
@property (nonatomic, strong, readonly) NSMeasurement<NSUnitPower *> * power;
```

## See Also

### Getting the connector information
- [var connector: CPChargingStationConnection.Connector](./connector-swift.property.md)
  The type of connector the station provides for vehicles.
- [var voltage: Measurement<UnitElectricPotentialDifference>](./voltage.md)
  The supported voltage level at the charging station.
- [CPChargingStationConnection.Connector](./connector-swift.enum.md)
  Constants for the connector types available at charging stations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/power)*