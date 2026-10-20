# init(scope:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a new map pitch toggle control with the provided scope.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope`: The namespace the framework passes to the associated [`Map`](../map.md) and [`mapScope(_:)`](../../SwiftUI/view/mapscope%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappitchtoggle/init(scope:))*