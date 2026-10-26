# actionSkipped(event:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

The function used to respond to action skipped events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
mutating func actionSkipped(event: Self.EventType)
```

#### Discussion

An event interval can be skipped due to scrubbing or a choppy frame rate. Necessary for stateful actions to maintain consistent state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/actionskipped(event:)-937ws)*