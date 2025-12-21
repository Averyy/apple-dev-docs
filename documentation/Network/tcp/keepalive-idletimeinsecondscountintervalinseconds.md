# keepalive(idleTimeInSeconds:count:intervalInSeconds:)

**Framework**: Network  
**Kind**: method

Enable TCP keepalives.

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
func keepalive(idleTimeInSeconds: UInt32, count: UInt32, intervalInSeconds: UInt32) -> TCP
```

## Parameters

- `idleTimeInSeconds`: The number of seconds of idleness to wait before keepalive   probes are sent by TCP ( ).
- `count`: The number of keepalive probes to send before terminating.
- `intervalInSeconds`: The number of seconds of to wait before resending TCP   keepalive probes ( ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/keepalive(idletimeinseconds:count:intervalinseconds:))*