# init(minimumDuration:maximumDistance:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
init(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must elapse before the gesture succeeds.
- `maximumDistance`: The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

- [init(minimumDuration: Double)](longpressgesture/init(minimumduration:).md)
  Creates a long-press gesture with a minimum duration
- [init(minimumDuration: Double, maximumDistance: CGFloat)](longpressgesture/init(minimumduration:maximumdistance:).md)
  Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [var minimumDuration: Double](longpressgesture/minimumduration.md)
  The minimum duration of the long press that must elapse before the gesture succeeds.
- [var maximumDistance: CGFloat](longpressgesture/maximumdistance.md)
  The maximum distance that the long press can move before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:inputkinds:))*