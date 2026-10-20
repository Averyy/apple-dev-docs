# remove(listener:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Stops listening to the event listener object.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func remove(listener: any GKGameSessionEventListener)
```

```objc
+ (void) removeEventListener:(NSObject<GKGameSessionEventListener> *) listener;
```

## Parameters

- `listener`: The `GKGameSessionEventListener` that is to be removed.

## See Also

### Listening for Events
- [class func add(listener: any GKGameSessionEventListener)](./add%28listener%29.md)
  Adds a new event listener object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/remove(listener:))*