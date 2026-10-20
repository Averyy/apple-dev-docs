# init(mapItem:displaysMap:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Create a map item detail view controller

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(mapItem: MKMapItem?, displaysMap: Bool)
```

```objc
- (instancetype) initWithMapItem:(MKMapItem *) mapItem displaysMap:(BOOL) displaysMap;
```

## Parameters

- `mapItem`: The map item to display, or `nil` to indicate the item is loading.
- `displaysMap`: Specify `true` to display an inline map with the place information. Specify `false` only if the application is already displaying a map view elsewhere.

## See Also

### Creating a map item detail view controller
- [init(mapItem: MKMapItem?)](./init%28mapitem%29.md)
  Create a map item detail view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller/init(mapitem:displaysmap:))*