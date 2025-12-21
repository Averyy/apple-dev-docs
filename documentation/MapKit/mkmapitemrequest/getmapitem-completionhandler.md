# getMapItem(completionHandler:)

**Framework**: MapKit  
**Kind**: method

Requests a map item and calls the provided completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var mapItem: MKMapItem { get async throws }
```

## Parameters

- `completionHandler`: A completion handler the framework calls to indicate the success or failure of the map item request.

## See Also

- [func cancel()](mkmapitemrequest/cancel.md)
  Cancels an in-progress map item request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/getmapitem(completionhandler:))*