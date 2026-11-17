# destinationNameVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.

**Availability**:
- iOS 17.4+ - Deprecated in 27.0
- iPadOS 17.4+ - Deprecated in 27.0
- Mac Catalyst 17.4+ - Deprecated in 27.0

## Declaration

```swift
var destinationNameVariants: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * destinationNameVariants;
```

## Discussion

You need to provide at least one variant. Present the variant strings as localized, displayable content.

## See Also

### Deprecated
- [convenience init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](./init%28origin,destination,routechoices%29.md)
  Creates a trip with an origin, destination, and route choices.
- [var origin: MKMapItem](./origin.md)
  The trip’s origin.
- [var destination: MKMapItem](./destination.md)
  The trip’s destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/destinationnamevariants)*