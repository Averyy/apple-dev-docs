# connectionTimeout(_:)

**Framework**: Network  
**Kind**: method

Set the timeout for TCP connection establishment.

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
func connectionTimeout(_ timeout: UInt32) -> TCP
```

#### Discussion

A timeout for TCP connection establishment, in seconds. (`TCP_CONNECTIONTIMEOUT`).

## Parameters

- `timeout`: The connection establishment timeout, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/connectiontimeout(_:))*