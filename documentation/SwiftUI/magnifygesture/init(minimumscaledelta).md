# init(minimumScaleDelta:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a magnify gesture with a given minimum delta for the gesture to start.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(minimumScaleDelta: CGFloat = 0.01)
```

## Parameters

- `minimumScaleDelta`: The minimum scale delta required before the gesture starts.

## See Also

### Creating the gesture
- [init(minimumScaleDelta: CGFloat, inputKinds: GestureInputKinds)](./init%28minimumscaledelta,inputkinds%29.md)
  Creates a magnify gesture with a given minimum delta for the gesture to start, and the input kinds the gesture recognizes.
- [var minimumScaleDelta: CGFloat](./minimumscaledelta.md)
  The minimum required delta before the gesture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/magnifygesture/init(minimumscaledelta:))*