# add(listener:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Adds a new event listener object.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func add(listener: any GKGameSessionEventListener)
```

```objc
+ (void) addEventListener:(NSObject<GKGameSessionEventListener> *) listener;
```

## Parameters

- `listener`: The `GKGameSessionEventLister` object being listened for.

## See Also

### Listening for Events
- [class func remove(listener: any GKGameSessionEventListener)](./remove%28listener%29.md)
  Stops listening to the event listener object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/add(listener:))*