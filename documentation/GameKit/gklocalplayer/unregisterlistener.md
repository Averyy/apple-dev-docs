# unregisterListener(_:)

**Framework**: GameKit  
**Kind**: method

Unregisters a listener object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func unregisterListener(_ listener: any GKLocalPlayerListener)
```

## Parameters

- `listener`: The object that GameKit stops sending messages to when events occur.

## See Also

- [func register(any GKLocalPlayerListener)](gklocalplayer/register(_:).md)
  Registers a listener for a particular event.
- [func unregisterAllListeners()](gklocalplayer/unregisteralllisteners.md)
  Unregisters all listeners in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/unregisterlistener(_:))*