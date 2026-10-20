# init(mapItem:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Create a map item detail view controller.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(mapItem: MKMapItem?)
```

```objc
- (instancetype) initWithMapItem:(MKMapItem *) mapItem;
```

#### Discussion

Displays an inline map with the place data.

## Parameters

- `mapItem`: The map item to display, or `nil` to indicate the item is loading.

## See Also

### Creating a map item detail view controller
- [init(mapItem: MKMapItem?, displaysMap: Bool)](./init%28mapitem,displaysmap%29.md)
  Create a map item detail view controller


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontroller/init(mapitem:))*