# init(mapFeatureAnnotation:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new map item request with the specified feature annotation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
init(mapFeatureAnnotation: MKMapFeatureAnnotation)
```

```objc
- (instancetype) initWithMapFeatureAnnotation:(MKMapFeatureAnnotation *) mapFeatureAnnotation;
```

## Parameters

- `mapFeatureAnnotation`: The [`MKMapFeatureAnnotation`](../mkmapfeatureannotation.md) to use to initialize the map item request.

## See Also

### Creating a request
- [convenience init(feature: MapFeature)](./init%28feature%29.md)
  Creates a new map item request with the specified map feature.
- [init(mapItemIdentifier: MKMapItem.Identifier)](./init%28mapitemidentifier%29.md)
  Create a request with a map item identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/init(mapfeatureannotation:))*