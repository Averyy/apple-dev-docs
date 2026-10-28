# shared()

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns the shared instance of the event handler.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
class func shared() -> GKTurnBasedEventHandler
```

```objc
+ (GKTurnBasedEventHandler *) sharedTurnBasedEventHandler;
```

## Return Value

An event handler object.

## Discussion

Your game never directly creates a [`GKTurnBasedEventHandler`](../gkturnbasedeventhandler.md) object. Instead, retrieve the shared instance using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/shared())*