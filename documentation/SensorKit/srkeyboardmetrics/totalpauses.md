# totalPauses

**Framework**: SensorKit  
**Kind**: property

The total number of pauses during the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var totalPauses: Int { get }
```

#### Discussion

The framework records a pause when the user stops entering text for more than 5 seconds.

## See Also

- [var totalWords: Int](srkeyboardmetrics/totalwords.md)
  The total number of typed words for the keyboard.
- [var totalAlteredWords: Int](srkeyboardmetrics/totalalteredwords.md)
  The total number of altered words for the keyboard.
- [var totalTaps: Int](srkeyboardmetrics/totaltaps.md)
  The total number of taps for the keyboard.
- [var totalDrags: Int](srkeyboardmetrics/totaldrags.md)
  The total number of drags for the keyboard.
- [var totalDeletes: Int](srkeyboardmetrics/totaldeletes.md)
  The total number of deletions for the keyboard.
- [var totalEmojis: Int](srkeyboardmetrics/totalemojis.md)
  The total number of emojis for the keyboard.
- [var totalPaths: Int](srkeyboardmetrics/totalpaths.md)
  The total number of completed paths for the keyboard.
- [var totalPathTime: TimeInterval](srkeyboardmetrics/totalpathtime.md)
  The total time to complete paths for the keyboard.
- [var totalPathLength: Measurement<UnitLength>](srkeyboardmetrics/totalpathlength.md)
  The total length of completed paths for the keyboard.
- [var totalAutoCorrections: Int](srkeyboardmetrics/totalautocorrections.md)
  The total number of autocorrections for the keyboard.
- [var totalSpaceCorrections: Int](srkeyboardmetrics/totalspacecorrections.md)
  The total number of space corrections for the keyboard.
- [var totalRetroCorrections: Int](srkeyboardmetrics/totalretrocorrections.md)
  The total number of retro corrections for the keyboard.
- [var totalTranspositionCorrections: Int](srkeyboardmetrics/totaltranspositioncorrections.md)
  The total number of transposition corrections for the keyboard.
- [var totalInsertKeyCorrections: Int](srkeyboardmetrics/totalinsertkeycorrections.md)
  The total number of Insert key corrections for the keyboard.
- [var totalSkipTouchCorrections: Int](srkeyboardmetrics/totalskiptouchcorrections.md)
  The total number of skip touch corrections for the keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/totalpauses)*