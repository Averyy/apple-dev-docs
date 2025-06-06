# init(minimumDuration:maximumDistance:)

**Framework**: SwiftUI  
**Kind**: init

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
init(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10)
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must   elapse before the gesture succeeds.
- `maximumDistance`: The maximum distance that the fingers or cursor   performing the long press can move before the gesture fails.

## See Also

- [init(minimumDuration: Double)](longpressgesture/init(minimumduration:).md)
  Creates a long-press gesture with a minimum duration
- [var minimumDuration: Double](longpressgesture/minimumduration.md)
  The minimum duration of the long press that must elapse before the gesture succeeds.
- [var maximumDistance: CGFloat](longpressgesture/maximumdistance.md)
  The maximum distance that the long press can move before the gesture fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:))*