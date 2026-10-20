# point(for:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Converts the specified map coordinate to a point in the coordinate space of the image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func point(for coordinate: CLLocationCoordinate2D) -> CGPoint
```

*macOS*

```swift
func point(for coordinate: CLLocationCoordinate2D) -> NSPoint
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (CGPoint) pointForCoordinate:(CLLocationCoordinate2D) coordinate;
```

*macOS*

```objc
- (NSPoint) pointForCoordinate:(CLLocationCoordinate2D) coordinate;
```

#### Return Value

The point in the image’s coordinate space that corresponds to the map location.

#### Discussion

If you want to display additional views or content on top of the image, you can use this method to find an appropriate point at which to draw those items.

## Parameters

- `coordinate`: A map coordinate that you want to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/point(for:))*