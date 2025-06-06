# UIApplication.State

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the running states of an app.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum State
```

## Topics

### Constants
- [UIApplication.State.active](uiapplication/state/active.md)
  The app is running in the foreground and currently receiving events.
- [UIApplication.State.inactive](uiapplication/state/inactive.md)
  The app is running in the foreground but isn’t receiving events.
- [UIApplication.State.background](uiapplication/state/background.md)
  The app is running in the background.
### Initializers
- [init?(rawValue: Int)](uiapplication/state/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var applicationState: UIApplication.State](uiapplication/applicationstate.md)
  The app’s current state, or that of its most active scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/state)*