# onServiceRegistrationUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the listener has added or removed a registered service.

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
final func onServiceRegistrationUpdate(_ handler: @escaping @isolated(any) (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.ServiceRegistrationChange) -> Void) -> Self
```

#### Discussion

The closure may be called multiple times until the listener is cancelled.

The closure inherits the isolation domain of the caller.

## Parameters

- `handler`: A handler to be called when a registered service changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/onserviceregistrationupdate(_:))*