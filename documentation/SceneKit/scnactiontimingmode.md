# SCNActionTimingMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Constants affecting the animation curve of an action, used by the [`timingMode`](./scnaction/timingmode.md) property.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNActionTimingMode
```

```c
enum SCNActionTimingMode : NSInteger;
```

## Topics

### Constants
- [SCNActionTimingMode.linear](./scnactiontimingmode/linear.md)
  Linear pacing. The animation progresses evenly throughout its duration.
- [SCNActionTimingMode.easeIn](./scnactiontimingmode/easein.md)
  Ease-in pacing. The animation begins slowly, and then speeds up as it progresses.
- [SCNActionTimingMode.easeOut](./scnactiontimingmode/easeout.md)
  Ease-out pacing. The animation begins quickly, and then slows as it completes.
- [SCNActionTimingMode.easeInEaseOut](./scnactiontimingmode/easeineaseout.md)
  Ease-in ease-out pacing. The animation begins slowly, accelerates through the middle of its duration, and then slows again before completing.
### Initializers
- [init?(rawValue: Int)](./scnactiontimingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [typealias SCNActionTimingFunction](./scnactiontimingfunction.md)
  The signature for a block that manages animation timing, used by the [`timingFunction`](./scnaction/timingfunction.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactiontimingmode)*