# userDecisions(in:)

**Framework**: Cinematic  
**Kind**: method

All user decisions in the given time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func userDecisions(in timeRange: CMTimeRange) -> [CNDecision]
```

#### Return Value

An array of user decisions in the given time range. These include user decisions made during recording or added to the script.

## Parameters

- `timeRange`: The time range of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/userdecisions(in:))*