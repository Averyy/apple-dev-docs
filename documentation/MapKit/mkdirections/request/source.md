# source

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The starting point for routing directions.

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
var source: MKMapItem? { get set }
```

```objc
@property (nonatomic, strong, nullable) MKMapItem * source;
```

## Discussion

Use the setter method `setSource:` to set this property.

## See Also

### Accessing the start and end points
- [var destination: MKMapItem?](./destination.md)
  The end point for routing directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/source)*