# setPredictionMode(_:for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Suggests how Siri should predict media intent shortcuts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setPredictionMode(_ mode: INUpcomingMediaPredictionMode, for type: INMediaItemType)
```

```objc
- (void) setPredictionMode:(INUpcomingMediaPredictionMode) mode forType:(INMediaItemType) type;
```

## Discussion

Apps such as podcast apps that want Siri to show only the suggested shortcuts—those set in the [`setSuggestedMediaIntents(_:)`](./setsuggestedmediaintents%28_%29.md) method and not media intents donated by your app for media the user has listened to or watched—should use the [`INUpcomingMediaPredictionMode.onlyPredictSuggestedIntents`](../inupcomingmediapredictionmode/onlypredictsuggestedintents.md) prediction mode. To tell Siri to show both donated and suggested media intent shortcuts associated with your app, use the [`INUpcomingMediaPredictionMode.default`](../inupcomingmediapredictionmode/default.md) mode or don’t set any prediction mode for the media type.

## Parameters

- `mode`: The prediction mode that Siri should use for your media intent shortcuts.
- `type`: The media type for this prediction mode.

## See Also

### Setting Prediction Modes
- [enum INUpcomingMediaPredictionMode](../inupcomingmediapredictionmode.md)
  Prediction modes for upcoming media intent shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediamanager/setpredictionmode(_:for:))*