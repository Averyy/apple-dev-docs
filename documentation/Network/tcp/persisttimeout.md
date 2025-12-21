# persistTimeout(_:)

**Framework**: Network  
**Kind**: method

Set the TCP persist timeout.

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
func persistTimeout(_ timeout: UInt32) -> TCP
```

#### Discussion

The TCP persist timeout, in seconds (`PERSIST_TIMEOUT`). See RFC 6429.

## Parameters

- `timeout`: The persist timeout, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/persisttimeout(_:))*