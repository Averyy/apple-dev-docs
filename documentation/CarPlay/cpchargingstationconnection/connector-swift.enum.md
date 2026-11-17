# CPChargingStationConnection.Connector

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants for the connector types available at charging stations.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Connector
```

```c
enum CPChargingStationConnectionConnector : NSInteger;
```

## Topics

### Enumeration Cases
- [CPChargingStationConnection.Connector.ccs1](./connector-swift.enum/ccs1.md)
  A combined charging system 1 (CCS1) connector.
- [CPChargingStationConnection.Connector.ccs2](./connector-swift.enum/ccs2.md)
  A combined charging system 2 (CCS2) connector.
- [CPChargingStationConnection.Connector.chaDeMo](./connector-swift.enum/chademo.md)
  A CHAdeMO connector with direct current.
- [CPChargingStationConnection.Connector.gbtAC](./connector-swift.enum/gbtac.md)
  A GB/T connector with alternating current.
- [CPChargingStationConnection.Connector.gbtDC](./connector-swift.enum/gbtdc.md)
  A GB/T connector with direct current.
- [CPChargingStationConnection.Connector.j1772](./connector-swift.enum/j1772.md)
  A J1772 connector with alternating current.
- [CPChargingStationConnection.Connector.mennekes](./connector-swift.enum/mennekes.md)
  A Mennekes connector.
- [CPChargingStationConnection.Connector.nacsAC](./connector-swift.enum/nacsac.md)
  A NACS connector with alternating current.
- [CPChargingStationConnection.Connector.nacsDC](./connector-swift.enum/nacsdc.md)
  A NACS connector with direct current.
### Initializers
- [init?(rawValue: Int)](./connector-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the connector information
- [var connector: CPChargingStationConnection.Connector](./connector-swift.property.md)
  The type of connector the station provides for vehicles.
- [var voltage: Measurement<UnitElectricPotentialDifference>](./voltage.md)
  The supported voltage level at the charging station.
- [var power: Measurement<UnitPower>](./power.md)
  The supported power level at the charging station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection/connector-swift.enum)*