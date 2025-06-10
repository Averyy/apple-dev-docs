# inboundStreams(_:)

**Framework**: Network  
**Kind**: method

Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection`, and multiple calls to run will throw an exception.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func inboundStreams(_ handler: @escaping @isolated(any) (NetworkConnection<QUIC>.SubConnection<QUICStream>) async throws -> Void) async throws
```

#### Discussion

If the `NetworkConnection` is not started at the time that `inboundStreams` is invoked, it will be started.

The closure inherits the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/inboundstreams(_:))*