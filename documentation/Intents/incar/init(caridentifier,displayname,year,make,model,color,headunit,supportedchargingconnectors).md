# init(carIdentifier:displayName:year:make:model:color:headUnit:supportedChargingConnectors:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a car object with the specified attributes, head unit, and supported charging connectors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(carIdentifier: String, displayName: String?, year: String?, make: String?, model: String?, color: CGColor?, headUnit: INCar.HeadUnit?, supportedChargingConnectors: [INCar.ChargingConnectorType])
```

```objc
- (instancetype) initWithCarIdentifier:(NSString *) carIdentifier displayName:(NSString *) displayName year:(NSString *) year make:(NSString *) make model:(NSString *) model color:(CGColorRef) color headUnit:(INCarHeadUnit *) headUnit supportedChargingConnectors:(NSArray<NSString *> *) supportedChargingConnectors;
```

## Discussion

The `carIdentifier` is a unique value that your app provides, and must not be the vehicle’s VIN or equivilent identifier. For the best user experience—and to prevent orphaned or duplicate vehicles in the user’s My Vehicles collection—your app must always provide the same identifier for the same vehicle.

Use `carIdentifier` when handling [`INGetCarPowerLevelStatusIntent`](../ingetcarpowerlevelstatusintent.md) requests so that the response can match the appropriate vehicle in the user’s Virtual Garage.

## Parameters

- `carIdentifier`: A unique identifier for the electric vehicle.
- `displayName`: A user-defined name for the electric vehicle that the system displays.
- `year`: The year of the electric vehicle’s manufacture.
- `make`: The electric vehicle’s manufacturer. Maps displays this value when it presents information about the electric vehicle.
- `model`: The manufacturer’s model name for the electric vehicle. Maps displays this value when it presents information about the electric vehicle.
- `color`: The color of the electric vehicle.
- `headUnit`: An instance of [`INCar.HeadUnit`](./headunit-swift.class.md) that contains the Bluetooth and iAP2 identifiers of the electric vehicle’s physical head unit.
- `supportedChargingConnectors`: An array of the electric vehicle’s supported charging connectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/init(caridentifier:displayname:year:make:model:color:headunit:supportedchargingconnectors:))*