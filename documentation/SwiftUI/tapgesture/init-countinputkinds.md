# init(count:inputKinds:)

**Framework**: SwiftUI  
**Kind**: init

Creates a tap gesture with the number of required taps and the input kinds the gesture recognizes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(count: Int = 1, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `count`: The required number of taps to complete the tap gesture.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

- [init(count: Int)](tapgesture/init(count:).md)
  Creates a tap gesture with the number of required taps.
- [var count: Int](tapgesture/count.md)
  The required number of tap events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tapgesture/init(count:inputkinds:))*