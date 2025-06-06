# polyline

**Framework**: MapKit  
**Kind**: property

The detailed route geometry.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var polyline: MKPolyline { get }
```

#### Discussion

The polyline object in this property reflects the complete path of the route, including all of its steps. You can use the polyline object as an overlay in a map view.

## See Also

- [var steps: [MKRoute.Step]](mkroute/steps.md)
  The array of steps that create the overall route.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/polyline)*