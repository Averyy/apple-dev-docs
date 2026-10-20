# CPRouteChoice

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A possible route for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPRouteChoice
```

```objc
@interface CPRouteChoice : NSObject
```

## Topics

### Creating a Route Choice
- [init(summaryVariants: [String], additionalInformationVariants: [String], selectionSummaryVariants: [String])](./cproutechoice/init%28summaryvariants,additionalinformationvariants,selectionsummaryvariants%29.md)
  Creates a route choice.
### Getting Variants
- [var summaryVariants: [String]](./cproutechoice/summaryvariants.md)
  An array of summary variants.
- [var additionalInformationVariants: [String]?](./cproutechoice/additionalinformationvariants.md)
  An array of variants providing additional information about the route choice.
- [var selectionSummaryVariants: [String]?](./cproutechoice/selectionsummaryvariants.md)
  An array of selection summary variants.
### Providing Additional Information
- [var userInfo: Any?](./cproutechoice/userinfo.md)
  An object containing custom information associated with the route choice.
### Initializers
- [init?(coder: NSCoder)](./cproutechoice/init%28coder%29.md)
- [init(summaryVariants: [String], additionalInformationVariants: [String], selectionSummaryVariants: [String], travelEstimates: CPTravelEstimates?)](./cproutechoice/init%28summaryvariants,additionalinformationvariants,selectionsummaryvariants,travelestimates%29.md)
  Initialize a @c CPRouteChoice with summary variants, additional information variants, selection summary variants, and travel estimates.
### Instance Properties
- [var travelEstimates: CPTravelEstimates?](./cproutechoice/travelestimates.md)
  Trip preview information such as battery, fuel, or toll information to display for this route choice.

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

### Creating a Trip
- [convenience init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](./cptrip/init%28origin,destination,routechoices%29.md)
  Creates a trip with an origin, destination, and route choices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice)*