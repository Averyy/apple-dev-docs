# removeObserver(_:)

**Framework**: AVSystemRouting  
**Kind**: method

Removes a previously registered observer from the system routing controller.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func removeObserver(_ observer: any AVSystemRouteControllerObserver)
```

#### Discussion

Call this function to unregister an observer when it no longer needs to receive routing event notifications. This is typically done in the observer’s deallocation or when the observer is no longer relevant to avoid memory leaks and unnecessary callbacks.

## Parameters

- `observer`: The observer object to remove. If the observer is not currently registered, this function has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-18ns8/removeobserver(_:))*