# destination

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The trip’s destination.

**Availability**:
- iOS 12.0+ - Deprecated in 26.4
- iPadOS 12.0+ - Deprecated in 26.4
- Mac Catalyst 13.1+ - Deprecated in 26.4

## Declaration

```swift
var destination: MKMapItem { get }
```

```objc
@property (nonatomic, strong, readonly) MKMapItem * destination;
```

## See Also

### Deprecated
- [convenience init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](./init%28origin,destination,routechoices%29.md)
  Creates a trip with an origin, destination, and route choices.
- [var origin: MKMapItem](./origin.md)
  The trip’s origin.
- [var destinationNameVariants: [String]?](./destinationnamevariants.md)
  An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/destination)*