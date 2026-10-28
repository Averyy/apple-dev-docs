# INUpcomingMediaPredictionMode.onlyPredictSuggestedIntents

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The mode that predicts suggested media intent shortcuts associated with your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case onlyPredictSuggestedIntents
```

```c
INUpcomingMediaPredictionModeOnlyPredictSuggestedIntents
```

## Discussion

Use this prediction mode when you want Siri to show the user only those media intent shortcuts set in the [`setSuggestedMediaIntents(_:)`](../inupcomingmediamanager/setsuggestedmediaintents%28_%29.md) method. For instance, a podcast app uses this mode when it wants to only show suggested shortcuts, rather than shortcuts it donated for media the user has already listened to or watched.

## See Also

### Prediction Modes
- [INUpcomingMediaPredictionMode.default](./default.md)
  The mode that predicts donated and suggested media intent shortcuts associated with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediapredictionmode/onlypredictsuggestedintents)*