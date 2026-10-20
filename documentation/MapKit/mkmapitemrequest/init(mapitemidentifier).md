# init(mapItemIdentifier:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Create a request with a map item identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(mapItemIdentifier identifier: MKMapItem.Identifier)
```

```objc
- (instancetype) initWithMapItemIdentifier:(MKMapItemIdentifier *) identifier;
```

## Parameters

- `identifier`: The identifier to use for the request.

## See Also

### Creating a request
- [convenience init(feature: MapFeature)](./init%28feature%29.md)
  Creates a new map item request with the specified map feature.
- [init(mapFeatureAnnotation: MKMapFeatureAnnotation)](./init%28mapfeatureannotation%29.md)
  Creates a new map item request with the specified feature annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/init(mapitemidentifier:))*