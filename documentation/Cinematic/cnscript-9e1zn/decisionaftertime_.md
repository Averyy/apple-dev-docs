# decisionAfterTime:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

The decision that occurs after the given time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNDecision *) decisionAfterTime:(CMTime) time;
```

## Return Value

The decision that occurred after the given time.

## Discussion

Pass the time of an existing decision to find the next one.

## Parameters

- `time`: The time of the decision to occur after.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/decisionaftertime:)*