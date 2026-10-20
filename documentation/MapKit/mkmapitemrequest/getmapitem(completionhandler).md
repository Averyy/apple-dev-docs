# getMapItem(completionHandler:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func getMapItem(completionHandler: @escaping @MainActor @Sendable (MKMapItem?, (any Error)?) -> Void)
```

```swift
var mapItem: MKMapItem { get async throws }
```

```objc
- (void) getMapItemWithCompletionHandler:(void (^)(MKMapItem *, NSError *)) completionHandler;
```

## Parameters

- `completionHandler`: A completion handler the framework calls to indicate the success or failure of the map item request.

## See Also

### Starting and stopping requests
- [func cancel()](./cancel%28%29.md)
  Cancels an in-progress map item request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/getmapitem(completionhandler:))*