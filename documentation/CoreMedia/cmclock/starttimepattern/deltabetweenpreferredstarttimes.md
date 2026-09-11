# deltaBetweenPreferredStartTimes

**Framework**: Core Media  
**Kind**: property

The delta between successive preferred start times.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var deltaBetweenPreferredStartTimes: CMTime
```

#### Discussion

Add integer multiples of this delta to `clockStartTime` and `hostClockStartTime` to calculate near-future preferred start times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/starttimepattern/deltabetweenpreferredstarttimes)*