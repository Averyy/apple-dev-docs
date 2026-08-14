# CPRouteDetail

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
class CPRouteDetail
```

#### Overview

Alongside standard routing details. This includes environmental data, vehicle consumption metrics, costs, and custom information specific to your app’s routing capabilities.

Route information appears in the route selection interface and during active navigation, helping users make informed decisions about their journey. The system automatically formats and displays this information using appropriate styling and placement.

Use route information to differentiate between routing options and provide transparency about journey characteristics. For example, display toll costs to help users choose between paid expressways and free alternatives, or show battery consumption for electric vehicles to ensure destination reachability.

> **Note**: Route information is supplementary to core routing details (distance, time, maneuvers). The system may choose to display some or all information based on available space and user context.

## Topics

### Initializers
- [convenience init(HOV: String)](cproutedetail/init(hov:)-hin7.md)
- [convenience init(batteryLevel: Double)](cproutedetail/init(batterylevel:).md)
  Creates additional route information for battery percentage.
- [convenience init(carbonFootprint: Measurement<UnitMass>)](cproutedetail/init(carbonfootprint:).md)
  Creates additional route information for carbon footprint.
- [init?(coder: NSCoder)](cproutedetail/init(coder:).md)
- [convenience init(ecoScore: Double)](cproutedetail/init(ecoscore:).md)
  Creates additional route information for an eco-score rating.
- [convenience init(emissions: Measurement<UnitMass>)](cproutedetail/init(emissions:).md)
  Creates additional route information for emissions data.
- [convenience init(fuelEnergy: Measurement<UnitEnergy>)](cproutedetail/init(fuelenergy:).md)
  Creates additional route information for fuel energy content.
- [convenience init(fuelLevel: Measurement<UnitVolume>)](cproutedetail/init(fuellevel:).md)
  Creates additional route information for a fuel level.
- [convenience init(fuelMass: Measurement<UnitMass>)](cproutedetail/init(fuelmass:).md)
  Creates additional route information for fuel mass.
- [convenience init(hov: String)](cproutedetail/init(hov:)-6ivii.md)
  Creates additional route information for High-Occupancy Vehicle (HOV) lane access.
- [convenience init(info: String)](cproutedetail/init(info:).md)
  Creates additional route information with a freeform informational string.
- [convenience init(kilowattHours: Measurement<UnitEnergy>)](cproutedetail/init(kilowatthours:).md)
  Creates additional route information for battery energy in kilowatt-hours.
- [convenience init(parking: String)](cproutedetail/init(parking:).md)
  Creates additional route information describing parking at the destination.
- [convenience init(rating: Double)](cproutedetail/init(rating:).md)
  Creates additional route information for a route rating.
- [convenience init(symbolName: String, value: String)](cproutedetail/init(symbolname:value:).md)
  Creates custom additional route information with a symbol name and value.
- [convenience init(tollAmount: Double, locale: Locale)](cproutedetail/init(tollamount:locale:).md)
  Creates additional route information for a toll amount.
- [convenience init(trafficLights: Int)](cproutedetail/init(trafficlights:).md)
  Creates additional route information for the number of traffic lights along the route.
- [convenience init(warning: String)](cproutedetail/init(warning:).md)
  Creates additional route information for route warnings.
### Instance Properties
- [var symbolTintColor: UIColor?](cproutedetail/symboltintcolor.md)
  The symbolTintColor to apply to the label.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail)*