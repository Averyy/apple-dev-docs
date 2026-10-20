# source

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The start point of the route.

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
var source: MKMapItem { get }
```

```objc
@property (nonatomic, readonly) MKMapItem * source;
```

#### Discussion

The item in this property may contain additional details that aren’t in the original item you use to create the [`MKDirections.Request`](../request.md) object.

## See Also

### Getting the end points
- [var destination: MKMapItem](./destination.md)
  The end point of the route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/response/source)*