# init(placeDescriptor:)

**Framework**: MapKit  
**Kind**: init

Creates a new map item request with the specified place descriptor

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
convenience init(placeDescriptor: PlaceDescriptor)
```

#### Return Value

An initialized map item object.

#### Discussion

Use this method to create a `MKMapItemRequest` from a [`PlaceDescriptor`](https://developer.apple.com/documentation/geotoolbox/placedescriptor) which you can then attempt to resolve asynchronously as shown here.

```swift
    Task {
        do {
            let request = MKMapItemRequest(placeDescriptor: descriptor)
            mapItem = try await request.mapItem
        } catch {
            handleLoadError(error, for: descriptor)
        }
    }
```

## Parameters

- `placeDescriptor`: The [`PlaceDescriptor`](https://developer.apple.com/documentation/geotoolbox/placedescriptor) the system should use to try to resolve information about desired map location. This parameter can’t be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/init(placedescriptor:))*