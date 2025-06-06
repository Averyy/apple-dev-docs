# CPRouteChoice

**Framework**: CarPlay  
**Kind**: class

A possible route for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPRouteChoice
```

## Topics

### Creating a Route Choice
- [init(summaryVariants: [String], additionalInformationVariants: [String], selectionSummaryVariants: [String])](cproutechoice/init(summaryvariants:additionalinformationvariants:selectionsummaryvariants:).md)
  Creates a route choice.
### Getting Variants
- [var summaryVariants: [String]](cproutechoice/summaryvariants.md)
  An array of summary variants.
- [var additionalInformationVariants: [String]?](cproutechoice/additionalinformationvariants.md)
  An array of variants providing additional information about the route choice.
- [var selectionSummaryVariants: [String]?](cproutechoice/selectionsummaryvariants.md)
  An array of selection summary variants.
### Providing Additional Information
- [var userInfo: Any?](cproutechoice/userinfo.md)
  An object containing custom information associated with the route choice.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](cptrip/init(origin:destination:routechoices:).md)
  Creates a trip with an origin, destination, and route choices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutechoice)*