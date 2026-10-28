# UIApplication.State.inactive

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The app is running in the foreground but isn’t receiving events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case inactive
```

```c
UIApplicationStateInactive
```

## Discussion

This might happen as a result of an interruption or because the app is transitioning to or from the background.

## See Also

### Constants
- [UIApplication.State.active](./active.md)
  The app is running in the foreground and currently receiving events.
- [UIApplication.State.background](./background.md)
  The app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/state/inactive)*