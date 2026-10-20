# init(minimumDuration:maximumDistance:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10)
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must elapse before the gesture succeeds.
- `maximumDistance`: The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.

## See Also

### Creating a long press gesture
- [init(minimumDuration: Double)](./init%28minimumduration%29.md)
  Creates a long-press gesture with a minimum duration
- [init(minimumDuration: Double, maximumDistance: CGFloat, inputKinds: GestureInputKinds)](./init%28minimumduration,maximumdistance,inputkinds%29.md)
  Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes.
- [var minimumDuration: Double](./minimumduration.md)
  The minimum duration of the long press that must elapse before the gesture succeeds.
- [var maximumDistance: CGFloat](./maximumdistance.md)
  The maximum distance that the long press can move before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:))*