# run(_:)

**Framework**: Network  
**Kind**: method

Run the listener and receive incoming connections.

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
final func run(_ handler: @escaping @isolated(any) (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws
```

#### Discussion

When the listener state moves to ready, the listener is registered with the system and can receive incoming connections.

`run()` should only be called once on a listener, and multiple calls to `run()` will throw an exception.

The closure inherits the isolation domain of the caller.

## Parameters

- `handler`: A handler to receive incoming connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/run(_:)-4iov3)*