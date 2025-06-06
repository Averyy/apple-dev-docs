# cancel()

**Framework**: Network Extension  
**Kind**: method

Cancel the session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Move into the `NWUDPSessionStateCancelled` state. The connection will be terminated, and all handlers will be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/cancel())*