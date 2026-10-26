# userDecisionsInTimeRange:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

All user decisions in the given time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (NSArray<CNDecision *> *) userDecisionsInTimeRange:(CMTimeRange) timeRange;
```

#### Return Value

An array of user decisions in the given time range. These include user decisions made during recording or added to the script.

## Parameters

- `timeRange`: The time range of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/userdecisionsintimerange:)*