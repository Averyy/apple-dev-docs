# shared()

**Framework**: GameKit  
**Kind**: method

Returns the shared instance of the event handler.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func shared() -> GKTurnBasedEventHandler
```

#### Return Value

An event handler object.

#### Discussion

Your game never directly creates a [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) object. Instead, retrieve the shared instance using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/shared())*