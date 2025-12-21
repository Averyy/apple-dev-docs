# canReplaceMapContent()

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value that indicates whether the overlay content replaces the underlying map content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func canReplaceMapContent() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the map view can skip the loading and drawing of the underlying map tiles, or [`false`](https://developer.apple.com/documentation/Swift/false) if the map view needs to draw the tiles.

#### Discussion

The map view uses the return value of this method as a hint to determine whether it loads and renders its tiles. If your overlay covers its designated region entirely with opaque content, and effectively replaces the content of underlying map tiles, implement this method and return [`true`](https://developer.apple.com/documentation/Swift/true). Doing so alleviates the need for the map to render its tiles.

If you don’t implement this method, or if you return [`false`](https://developer.apple.com/documentation/Swift/false) from it, the map view continues to load and render its tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlay/canreplacemapcontent())*