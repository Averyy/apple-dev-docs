# init(_:coordinate:)

**Framework**: MapKit  
**Kind**: init

Creates a marker at the given location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D) where Label == Text
```

## Parameters

- `titleResource`: The localized string for the title.
- `coordinate`: The coordinate to display the marker at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker/init(_:coordinate:)-3bjj6)*