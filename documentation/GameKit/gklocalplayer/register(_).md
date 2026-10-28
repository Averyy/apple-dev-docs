# register(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) registerListener:(id<GKLocalPlayerListener>) listener;
```

## Discussion

Only register a listener a single time. Registering a listener multiple times results in undefined behavior.

## Parameters

- `listener`: The object that GameKit sends messages to when events occur.

## See Also

### Registering Listeners
- [func unregisterAllListeners()](./unregisteralllisteners%28%29.md)
  Unregisters all listeners in your game.
- [func unregisterListener(any GKLocalPlayerListener)](./unregisterlistener%28_%29.md)
  Unregisters a listener object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/register(_:))*