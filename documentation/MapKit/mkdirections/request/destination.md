# destination

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The end point for routing directions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var destination: MKMapItem? { get set }
```

```objc
@property (nonatomic, strong, nullable) MKMapItem * destination;
```

#### Discussion

Use the setter method `setDestination:` to set this property.

## See Also

### Accessing the start and end points
- [var source: MKMapItem?](./source.md)
  The starting point for routing directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/destination)*