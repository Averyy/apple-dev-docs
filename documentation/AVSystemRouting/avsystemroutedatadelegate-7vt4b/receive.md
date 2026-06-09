# receive(_:)

**Framework**: AVSystemRouting  
**Kind**: method  
**Required**: Yes

Receives data sent from a connected remote applicaiton.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func receive(_ data: Data) async throws
```

#### Discussion

> **Note**: An error if processing the received data fails.

## Parameters

- `data`: The data received from the remote app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutedatadelegate-7vt4b/receive(_:))*