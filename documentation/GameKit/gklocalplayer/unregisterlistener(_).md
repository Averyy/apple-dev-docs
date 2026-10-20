# unregisterListener(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) unregisterListener:(id<GKLocalPlayerListener>) listener;
```

## Parameters

- `listener`: The object that GameKit stops sending messages to when events occur.

## See Also

### Registering Listeners
- [func register(any GKLocalPlayerListener)](./register%28_%29.md)
  Registers a listener for a particular event.
- [func unregisterAllListeners()](./unregisteralllisteners%28%29.md)
  Unregisters all listeners in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/unregisterlistener(_:))*