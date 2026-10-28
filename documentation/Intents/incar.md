# INCar

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A specific electric vehicle that Maps uses during route planning and navigation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INCar
```

```objc
@interface INCar : NSObject
```

## Overview

An `INCar` object provides information about a specific electric vehicle that belongs to the user.

When planning a route, Maps may use an [`INListCarsIntent`](./inlistcarsintent.md) intent to ask your app to provide a list of the user’s electric vehicles. In your handler, determine which of the user’s vehicles respond to [`INGetCarPowerLevelStatusIntent`](./ingetcarpowerlevelstatusintent.md), and create an instance of `INCar` for each. You then assign these instances to the [`cars`](./inlistcarsintentresponse/cars.md) property of your response object. When navigation begins using one of these vehicles, Maps regularly requests updates of the power level status using `INGetCarPowerLevelStatusIntent`.

For more information on handling `INListCarsIntent`, see [`INListCarsIntentHandling`](./inlistcarsintenthandling.md).

## Topics

### Creating a Car
- [init(carIdentifier: String, displayName: String?, year: String?, make: String?, model: String?, color: CGColor?, headUnit: INCar.HeadUnit?, supportedChargingConnectors: [INCar.ChargingConnectorType])](./incar/init%28caridentifier,displayname,year,make,model,color,headunit,supportedchargingconnectors%29.md)
  Creates a car object with the specified attributes, head unit, and supported charging connectors.
### Identifying the Car
- [var carIdentifier: String](./incar/caridentifier.md)
  The electric vehicle’s unique identifier.
- [var displayName: String?](./incar/displayname.md)
  The electric vehicle’s user-defined display name.
### Getting the Car’s Attributes
- [var make: String?](./incar/make.md)
  The electric vehicle’s manufacturer.
- [var model: String?](./incar/model.md)
  The manufacturer’s model name for the electric vehicle.
- [var color: CGColor?](./incar/color.md)
  The electric vehicle’s color.
- [var year: String?](./incar/year.md)
  The electric vehicle’s year of manufacture.
### Getting the Car’s Head Unit
- [var headUnit: INCar.HeadUnit?](./incar/headunit-swift.property.md)
  The Bluetooth and iAP2 identifiers of the electric vehicle’s physical head unit.
- [INCar.HeadUnit](./incar/headunit-swift.class.md)
  An object that contains the Bluetooth and iAP2 identifiers of the vehicle’s physical head unit.
### Getting the Car’s Supported Charging Connectors
- [var supportedChargingConnectors: [INCar.ChargingConnectorType]](./incar/supportedchargingconnectors.md)
  The charging connectors that the electric vehicle supports.
- [struct ChargingConnectorType](./incar/chargingconnectortype.md)
  Constants that describe the available charging connector types.
### Providing a Charging Connector’s Maximum Power
- [func maximumPower(for: INCar.ChargingConnectorType) -> Measurement<UnitPower>?](./incar/maximumpower%28for%29.md)
  Gets the maximum power for a specific type of charging connector.
- [func setMaximumPower(Measurement<UnitPower>, for: INCar.ChargingConnectorType)](./incar/setmaximumpower%28_,for%29.md)
  Sets the maximum power for a specific type of charging connector.
### Initializers
- [init?(coder: NSCoder)](./incar/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Providing a List of Cars
- [var cars: [INCar]?](./inlistcarsintentresponse/cars.md)
  An array of the user’s electric vehicles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar)*