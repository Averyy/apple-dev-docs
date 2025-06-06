# decision(at:tolerance:)

**Framework**: Cinematic  
**Kind**: method

The closest decision to the given time within the given tolerance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func decision(at time: CMTime, tolerance: CMTime) -> CNDecision?
```

#### Return Value

A decision representing the closest decision to the given time within the given tolerance. Returns nil if there are none.

## Parameters

- `time`: The time of the decision.
- `tolerance`: The tolerance time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/decision(at:tolerance:))*