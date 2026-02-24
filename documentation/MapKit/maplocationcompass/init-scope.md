# init(scope:)

**Framework**: MapKit  
**Kind**: init

Creates a new map location compass with the provided scope.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope`: The namespace the framework passes to the associated [`Map`](map.md) and `MapLocationCompass/mapScope(_:)`. For use outside of `MapLocationCompass/mapControls(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/maplocationcompass/init(scope:))*