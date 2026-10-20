# preferredLocale

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates the preferred locale for the addresses the request returns, or `nil` if the framework should use the device locale.

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
var preferredLocale: Locale? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSLocale * preferredLocale;
```

## See Also

### Getting information about map items and the reverse geocoder’s locale’
- [func getMapItems(completionHandler: ([MKMapItem]?, (any Error)?) -> Void)](./getmapitems%28completionhandler%29.md)
  Returns the map items relevant to the reverse geocoded location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/preferredlocale)*