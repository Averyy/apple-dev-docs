# KeyPress.Result

**Framework**: SwiftUI  
**Kind**: enum

A result value returned from a key-press action that indicates whether the action consumed the event.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum Result
```

## Topics

### Getting the result
- [KeyPress.Result.handled](keypress/result/handled.md)
  The action consumed the event, preventing dispatch from continuing.
- [KeyPress.Result.ignored](keypress/result/ignored.md)
  The action ignored the event, allowing dispatch to continue.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keypress/result)*