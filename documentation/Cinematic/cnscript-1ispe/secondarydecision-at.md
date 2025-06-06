# secondaryDecision(at:)

**Framework**: Cinematic  
**Kind**: method

If a given time is during a focus transition, the system transitions toward a secondary decision.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func secondaryDecision(at time: CMTime) -> CNDecision?
```

#### Return Value

The secondary decision the system is transitioning toward for the given time.

## Parameters

- `time`: The time of the focus transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/secondarydecision(at:))*