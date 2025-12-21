# onStateUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the listener’s state changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@discardableResult
final func onStateUpdate(_ handler: @escaping @isolated(any) (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.State) -> Void) -> Self
```

#### Discussion

The closure may be called multiple times until the listener is cancelled.

The closure inherits the isolation domain of the caller.

## Parameters

- `handler`: A handler to be called with state updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/onstateupdate(_:))*