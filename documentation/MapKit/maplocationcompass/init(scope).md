# init(scope:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new map location compass with the provided scope.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope`: The namespace the framework passes to the associated [`Map`](../map.md) and [`mapScope(_:)`](../../SwiftUI/view/mapscope%28_%29.md). For use outside of [`mapControls(_:)`](../../SwiftUI/view/mapcontrols%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/maplocationcompass/init(scope:))*