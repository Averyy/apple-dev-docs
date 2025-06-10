# decode(_:)

**Framework**: MapKit  
**Kind**: method

Decodes the provided data into native MapKit types that a map can display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func decode(_ data: Data) throws -> [any MKGeoJSONObject]
```

#### Return Value

An array of [`MKGeoJSONObject`](mkgeojsonobject.md) objects, or an error if the decoder encounters an issue.

## Parameters

- `data`: An   object that contains the JSON to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsondecoder/decode(_:))*