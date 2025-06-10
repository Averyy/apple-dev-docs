# init(_:image:coordinate:)

**Framework**: MapKit  
**Kind**: init

Creates a marker at the given location with an image displayed as the balloon’s icon.

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
@preconcurrency init(_ titleResource: LocalizedStringResource, image: String, coordinate: CLLocationCoordinate2D) where Label == Label<Text, Image>
```

## Parameters

- `titleResource`: The localized string for the title.
- `image`: The name of the image resource to look up and use as   the marker balloon’s glyph.
- `coordinate`: The coordinate to display the marker at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/marker/init(_:image:coordinate:)-1q3pz)*