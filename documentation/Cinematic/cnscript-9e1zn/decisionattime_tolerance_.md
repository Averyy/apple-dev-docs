# decisionAtTime:tolerance:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

The closest frame to the given time within the given tolerance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNDecision *) decisionAtTime:(CMTime) time tolerance:(CMTime) tolerance;
```

## Return Value

The closest frame to the time of interest within the given tolerance.

## Parameters

- `time`: The time of interest.
- `tolerance`: The tolerance time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/decisionattime:tolerance:)*