# init(minimumScaleDelta:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a magnify gesture with a given minimum delta for the gesture to start, and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(minimumScaleDelta: CGFloat = 0.01, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumScaleDelta`: The minimum scale delta required before the gesture starts.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

- [init(minimumScaleDelta: CGFloat)](magnifygesture/init(minimumscaledelta:).md)
  Creates a magnify gesture with a given minimum delta for the gesture to start.
- [var minimumScaleDelta: CGFloat](magnifygesture/minimumscaledelta.md)
  The minimum required delta before the gesture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/magnifygesture/init(minimumscaledelta:inputkinds:))*