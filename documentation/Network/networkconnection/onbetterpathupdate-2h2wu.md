# onBetterPathUpdate(_:)

**Framework**: Network  
**Kind**: method

A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
final func onBetterPathUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkConnection<ApplicationProtocol>, Bool) -> Void) -> Self
```

#### Discussion

Set a closure to be called when a better path becomes available or unavailable, which may be called multiple times until the connection is cancelled.

When a better path is available, if it is possible to migrate work from this connection to a new connection, create a new connection to the endpoint. Continue doing work on this connection until the new connection is ready. Once ready, transition work to the new connection and cancel this one.

This closure will inherit the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/onbetterpathupdate(_:)-2h2wu)*