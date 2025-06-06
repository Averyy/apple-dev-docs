# register(_:)

**Framework**: GameKit  
**Kind**: method

Registers a listener for a particular event.

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
func register(_ listener: any GKLocalPlayerListener)
```

#### Discussion

Only register a listener a single time. Registering a listener multiple times results in undefined behavior.

## Parameters

- `listener`: The object that GameKit sends messages to when events occur.

## See Also

- [func unregisterAllListeners()](gklocalplayer/unregisteralllisteners.md)
  Unregisters all listeners in your game.
- [func unregisterListener(any GKLocalPlayerListener)](gklocalplayer/unregisterlistener(_:).md)
  Unregisters a listener object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/register(_:))*