# init(minimumDuration:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a long-press gesture with a minimum duration

**Availability**:
- tvOS 14.0+

## Declaration

```swift
nonisolated
init(minimumDuration: Double = 0.5)
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must elapse before the gesture succeeds.

## See Also

### Creating a long press gesture
- [init(minimumDuration: Double, maximumDistance: CGFloat)](./init%28minimumduration,maximumdistance%29.md)
  Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [init(minimumDuration: Double, maximumDistance: CGFloat, inputKinds: GestureInputKinds)](./init%28minimumduration,maximumdistance,inputkinds%29.md)
  Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes.
- [var minimumDuration: Double](./minimumduration.md)
  The minimum duration of the long press that must elapse before the gesture succeeds.
- [var maximumDistance: CGFloat](./maximumdistance.md)
  The maximum distance that the long press can move before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:))*