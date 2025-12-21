# idleTimeout(_:)

**Framework**: Network  
**Kind**: method

Set the idle timeout for the QUIC connection, in milliseconds.

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
func idleTimeout(_ timeout: Int) -> QUIC
```

#### Discussion

If no packets are sent or received within this timeout, the QUIC connection will be closed.

## Parameters

- `timeout`: The idle timeout, in milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quic/idletimeout(_:))*