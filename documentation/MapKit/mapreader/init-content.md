# init(content:)

**Framework**: MapKit  
**Kind**: init

Creates an instance that allows view content to reference information about a contained map.

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
@preconcurrency init(@ViewBuilder content: @escaping (MapProxy) -> Content)
```

#### Return Value

Returns a [`MapProxy`](mapproxy.md) that allows you to introspect the content of a map.

## Parameters

- `content`: The content of the map reader uses to retrieve information about, it uses the first map the   contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapreader/init(content:))*