# INCar.ChargingConnectorType

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants that describe the available charging connector types.

## Declaration

```swift
struct ChargingConnectorType
```

```c
typedef NSString * INCarChargingConnectorType;
```

## Topics

### Creating a Charging Connector Type
- [init(rawValue: String)](./chargingconnectortype/init%28rawvalue%29.md)
  Creates a charging connector type using the provided string.
### Charging Connector Types
- [static let ccs1: INCar.ChargingConnectorType](./chargingconnectortype/ccs1.md)
  The CCS1 charging connector type.
- [static let ccs2: INCar.ChargingConnectorType](./chargingconnectortype/ccs2.md)
  The CCS2 charging connector type.
- [static let chaDeMo: INCar.ChargingConnectorType](./chargingconnectortype/chademo.md)
  The CHAdeMO charging connector type.
- [static let gbtAC: INCar.ChargingConnectorType](./chargingconnectortype/gbtac.md)
  The GB/T AC charging connector type for alternating current.
- [static let gbtDC: INCar.ChargingConnectorType](./chargingconnectortype/gbtdc.md)
  The GB/T DC charging connector type for direct current.
- [static let j1772: INCar.ChargingConnectorType](./chargingconnectortype/j1772.md)
  The J1772 charging connector type.
- [static let mennekes: INCar.ChargingConnectorType](./chargingconnectortype/mennekes.md)
  The Mennekes charging connector type.
- [static let tesla: INCar.ChargingConnectorType](./chargingconnectortype/tesla.md)
  The charging connector type for Tesla electric vehicles.
### Type Properties
- [static let nacsAC: INCar.ChargingConnectorType](./chargingconnectortype/nacsac.md)
- [static let nacsDC: INCar.ChargingConnectorType](./chargingconnectortype/nacsdc.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Car’s Supported Charging Connectors
- [var supportedChargingConnectors: [INCar.ChargingConnectorType]](./supportedchargingconnectors.md)
  The charging connectors that the electric vehicle supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/chargingconnectortype)*