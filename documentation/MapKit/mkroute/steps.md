# steps

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The array of steps that create the overall route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var steps: [MKRoute.Step] { get }
```

```objc
@property (nonatomic, readonly) NSArray<MKRouteStep *> * steps;
```

## Discussion

The array contains one or more [`MKRoute.Step`](./step.md) objects representing distinct portions of the route. Each step corresponds to a single direction that must be followed along the route.

## See Also

### Getting the route geometry
- [var polyline: MKPolyline](./polyline.md)
  The detailed route geometry.
- [MKRoute.Step](./step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/steps)*