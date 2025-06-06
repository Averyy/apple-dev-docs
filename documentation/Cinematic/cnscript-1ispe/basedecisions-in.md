# baseDecisions(in:)

**Framework**: Cinematic  
**Kind**: method

All base decisions made automatically during recording in the given time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func baseDecisions(in timeRange: CMTimeRange) -> [CNDecision]
```

#### Return Value

An array of base decisions in a given time range. These apply if no user decision overrides them.

## Parameters

- `timeRange`: The time range of the base decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/basedecisions(in:))*