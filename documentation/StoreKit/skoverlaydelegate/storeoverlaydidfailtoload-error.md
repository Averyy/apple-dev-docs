# storeOverlayDidFailToLoad(_:error:)

**Framework**: StoreKit  
**Kind**: method

Indicates that an overlay failed to load.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func storeOverlayDidFailToLoad(_ overlay: SKOverlay, error: any Error)
```

#### Discussion

Common cases for a failure when loading an overlay are:

- Using invalid iTunes identifiers.
- Trying to present an overlay for media that’s not an app.
- Trying to present an overlay from an app extension or the simulator.

## Parameters

- `overlay`: An overlay object that failed to load.
- `error`: An indication of why the overlay failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfailtoload(_:error:))*