# init(minimumAngleDelta:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a rotation gesture with a minimum delta for the gesture to start, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(minimumAngleDelta: Angle = .degrees(1), inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumAngleDelta`: The minimum delta required before the gesture starts. The default value is a one-degree angle.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

- [init(minimumAngleDelta: Angle)](rotategesture/init(minimumangledelta:).md)
  Creates a rotation gesture with a minimum delta for the gesture to start.
- [var minimumAngleDelta: Angle](rotategesture/minimumangledelta.md)
  The minimum delta required before the gesture succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotategesture/init(minimumangledelta:inputkinds:))*