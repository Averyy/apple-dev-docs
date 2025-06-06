# actionSkipped(event:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

The function used to respond to action skipped events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
mutating func actionSkipped(event: Self.EventType)
```

#### Discussion

The animation system can skip over an event interval due to scrubbing or choppy frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/actionskipped(event:))*