# INGetCarPowerLevelStatusIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request for the vehicle power level.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INGetCarPowerLevelStatusIntentResponse
```

```objc
@interface INGetCarPowerLevelStatusIntentResponse : INIntentResponse
```

## Overview

Use an `INGetCarPowerLevelStatusIntentResponse` object to specify the result of a request for a vehicle’s current power level. You create instances of this class when confirming or handling a power level status intent, or when reporting abrupt changes in an electric vehicle’s battery charge. Use this object to confirm that the request is valid, to communicate whether the app receives the power level data from the vehicle, or to report any errors that occur.

You create an `INGetCarPowerLevelStatusIntentResponse` object in the [`confirm(intent:completion:)`](./ingetcarpowerlevelstatusintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./ingetcarpowerlevelstatusintenthandling/handle%28intent,completion%29.md) methods of your intent handler object, and when calling [`didUpdate(getCarPowerLevelStatus:)`](./ingetcarpowerlevelstatusintentresponseobserver/didupdate%28getcarpowerlevelstatus%29.md) to notify Maps about abrupt battery charge changes in the user’s electric vehicle.

For more information about implementing your intent handler object, see [`INGetCarPowerLevelStatusIntentHandling`](./ingetcarpowerlevelstatusintenthandling.md).

## Topics

### Creating a Response Object
- [init(code: INGetCarPowerLevelStatusIntentResponseCode, userActivity: NSUserActivity?)](./ingetcarpowerlevelstatusintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity.
### Getting the Response Code
- [var code: INGetCarPowerLevelStatusIntentResponseCode](./ingetcarpowerlevelstatusintentresponse/code.md)
  The code that indicates success or failure when confirming or handling an intent.
- [enum INGetCarPowerLevelStatusIntentResponseCode](./ingetcarpowerlevelstatusintentresponsecode.md)
  Constants that indicate the status of the response.
### Identifying the Vehicle
- [var carIdentifier: String?](./ingetcarpowerlevelstatusintentresponse/caridentifier.md)
  A unique identifier for the vehicle.
### Providing Fuel, Charge, and Distance Information
- [var chargePercentRemaining: Float?](./ingetcarpowerlevelstatusintentresponse/chargepercentremaining-51zwv.md)
  The percentage of charge that remains for the electric vehicle.
- [var fuelPercentRemaining: Float?](./ingetcarpowerlevelstatusintentresponse/fuelpercentremaining-56xw3.md)
  The percentage of fuel that remains for the fuel-powered vehicle.
- [var maximumDistance: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/maximumdistance.md)
  The maximum rated distance the vehicle can travel with full resources.
- [var distanceRemaining: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/distanceremaining.md)
  The maximum distance the vehicle can travel with the remaining resources.
- [var maximumDistanceElectric: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/maximumdistanceelectric.md)
  The maximum rated distance the electric vehicle can travel on a full charge.
- [var distanceRemainingElectric: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/distanceremainingelectric.md)
  The maximum distance the electric vehicle can travel with the remaining charge.
- [var maximumDistanceFuel: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/maximumdistancefuel.md)
  The maximum rated distance the fuel-powered vehicle can travel with a full tank of fuel.
- [var distanceRemainingFuel: Measurement<UnitLength>?](./ingetcarpowerlevelstatusintentresponse/distanceremainingfuel.md)
  The maximum distance the fuel-powered vehicle can travel with the remaining fuel.
- [chargePercentRemaining](./ingetcarpowerlevelstatusintentresponse/chargepercentremaining-30zol.md)
  The percentage of charge that remains for the electric vehicle.
- [fuelPercentRemaining](./ingetcarpowerlevelstatusintentresponse/fuelpercentremaining-6mdv4.md)
  The percentage of fuel remaining for the fuel-powered vehicle.
### Providing the Charge Status
- [var activeConnector: INCar.ChargingConnectorType?](./ingetcarpowerlevelstatusintentresponse/activeconnector.md)
  The type of connector that’s currently delivering charge to the electric vehicle’s battery.
- [var charging: Bool?](./ingetcarpowerlevelstatusintentresponse/charging-6xnqj.md)
  A Boolean value that indicates whether the electric vehicle is currently charging.
- [var minutesToFull: Int?](./ingetcarpowerlevelstatusintentresponse/minutestofull-2kbt6.md)
  The number of minutes it takes to fully charge the electric vehicle’s battery.
- [var dateOfLastStateUpdate: DateComponents?](./ingetcarpowerlevelstatusintentresponse/dateoflaststateupdate.md)
  A timestamp that indicates the most recent charge status for the electric vehicle.
- [charging](./ingetcarpowerlevelstatusintentresponse/charging-7aamu.md)
  A Boolean value that indicates whether the electric vehicle is currently charging.
- [minutesToFull](./ingetcarpowerlevelstatusintentresponse/minutestofull-25vcb.md)
  The number of minutes it will take to fully charge the electric vehicle’s battery.
### Providing Battery Capacity
- [var minimumBatteryCapacity: Measurement<UnitEnergy>?](./ingetcarpowerlevelstatusintentresponse/minimumbatterycapacity.md)
  A user-facing value that represents the minimum battery capacity of the electric vehicle.
- [var maximumBatteryCapacity: Measurement<UnitEnergy>?](./ingetcarpowerlevelstatusintentresponse/maximumbatterycapacity.md)
  A user-facing value that represents the maximum battery capacity of the electric vehicle.
- [var currentBatteryCapacity: Measurement<UnitEnergy>?](./ingetcarpowerlevelstatusintentresponse/currentbatterycapacity.md)
  A user-facing value that represents the current battery capacity of the electric vehicle.
### Providing Formula Arguments
- [var chargingFormulaArguments: [String : Any]?](./ingetcarpowerlevelstatusintentresponse/chargingformulaarguments.md)
  The parameters the electric vehicle’s charging model uses to calculate the duration of a charge.
- [var consumptionFormulaArguments: [String : Any]?](./ingetcarpowerlevelstatusintentresponse/consumptionformulaarguments.md)
  The parameters the electric vehicle’s consumption model uses to calculate its energy consumption.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
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

### Get Car Power Level Status
- [protocol INGetCarPowerLevelStatusIntentHandling](./ingetcarpowerlevelstatusintenthandling.md)
  The handler interface for requesting a car’s current power level.
- [class INGetCarPowerLevelStatusIntent](./ingetcarpowerlevelstatusintent.md)
  A request for the current power level of the user’s car.
- [protocol INGetCarPowerLevelStatusIntentResponseObserver](./ingetcarpowerlevelstatusintentresponseobserver.md)
  The interface for providing updates of a vehicle’s power level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse)*