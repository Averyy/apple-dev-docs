# init(coder:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a camera boundary using the provided coder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The decoder to use during initialization.

## See Also

### Creating a camera boundary
- [init?(coordinateRegion: MKCoordinateRegion)](./init%28coordinateregion%29.md)
  Creates a camera boundary using the provided coordinate region.
- [init?(mapRect: MKMapRect)](./init%28maprect%29.md)
  Creates a camera boundary using the provided map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class/init(coder:))*