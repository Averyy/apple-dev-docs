# SCNActionTimingMode

**Framework**: SceneKit  
**Kind**: enum

Constants affecting the animation curve of an action, used by the [`timingMode`](scnaction/timingmode.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SCNActionTimingMode
```

## Topics

### Constants
- [SCNActionTimingMode.linear](scnactiontimingmode/linear.md)
  Linear pacing. The animation progresses evenly throughout its duration.
- [SCNActionTimingMode.easeIn](scnactiontimingmode/easein.md)
  Ease-in pacing. The animation begins slowly, and then speeds up as it progresses.
- [SCNActionTimingMode.easeOut](scnactiontimingmode/easeout.md)
  Ease-out pacing. The animation begins quickly, and then slows as it completes.
- [SCNActionTimingMode.easeInEaseOut](scnactiontimingmode/easeineaseout.md)
  Ease-in ease-out pacing. The animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.
### Initializers
- [init?(rawValue: Int)](scnactiontimingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias SCNActionTimingFunction](scnactiontimingfunction.md)
  The signature for a block that manages animation timing, used by the [`timingFunction`](scnaction/timingfunction.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactiontimingmode)*