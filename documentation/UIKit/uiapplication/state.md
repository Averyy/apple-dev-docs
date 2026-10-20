# UIApplication.State

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the running states of an app.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum State
```

```c
enum UIApplicationState : NSInteger;
```

## Topics

### Constants
- [UIApplication.State.active](./state/active.md)
  The app is running in the foreground and currently receiving events.
- [UIApplication.State.inactive](./state/inactive.md)
  The app is running in the foreground but isn’t receiving events.
- [UIApplication.State.background](./state/background.md)
  The app is running in the background.
### Initializers
- [init?(rawValue: Int)](./state/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the application state
- [var applicationState: UIApplication.State](./applicationstate.md)
  The app’s current state, or that of its most active scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/state)*