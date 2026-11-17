# init(origin:destination:routeChoices:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a trip with an origin, destination, and route choices.

**Availability**:
- iOS 12.0+ - Deprecated in 26.4
- iPadOS 12.0+ - Deprecated in 26.4
- Mac Catalyst 13.1+ - Deprecated in 26.4

## Declaration

```swift
convenience init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])
```

```objc
- (instancetype) initWithOrigin:(MKMapItem *) origin destination:(MKMapItem *) destination routeChoices:(NSArray<CPRouteChoice *> *) routeChoices;
```

## Return Value

A newly initialized trip.

## Parameters

- `origin`: The trip’s origin.
- `destination`: The trip’s destination.
- `routeChoices`: Up to three route choices available for the trip.

## See Also

### Deprecated
- [var origin: MKMapItem](./origin.md)
  The trip’s origin.
- [var destination: MKMapItem](./destination.md)
  The trip’s destination.
- [var destinationNameVariants: [String]?](./destinationnamevariants.md)
  An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/init(origin:destination:routechoices:))*