# getMapItems(completionHandler:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the map items relevant to the reverse geocoded location.

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
func getMapItems(completionHandler: @escaping @MainActor @Sendable ([MKMapItem]?, (any Error)?) -> Void)
```

```swift
var mapItems: [MKMapItem] { get async throws }
```

```objc
- (void) getMapItemsWithCompletionHandler:(void (^)(NSArray<MKMapItem *> *, NSError *)) completionHandler;
```

## See Also

### Getting information about map items and the reverse geocoder’s locale’
- [var preferredLocale: Locale?](./preferredlocale.md)
  A value that indicates the preferred locale for the addresses the request returns, or `nil` if the framework should use the device locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/getmapitems(completionhandler:))*