# primaryDecisionAtTime:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

The primary decision that’s in effect at the specified time, unless it’s outside the time range of the Cinematic script.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNDecision *) primaryDecisionAtTime:(CMTime) time;
```

## Return Value

A value representing the primary decision that’s in effect at the specified time, unless it’s outside the time range of the Cinematic script. The value also represents the decision being transitioned away from the given time is during a focus transition.

## Parameters

- `time`: The time of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/primarydecisionattime:)*