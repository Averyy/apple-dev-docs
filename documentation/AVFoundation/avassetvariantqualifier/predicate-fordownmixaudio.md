# predicate(forDownmixAudio:)

**Framework**: AVFoundation  
**Kind**: method

Creates a NSPredicate for immersive audio which can be used with other NSPredicates to express variant preferences.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
class func predicate(forDownmixAudio isDownmixAudio: Bool) -> NSPredicate
```

#### Discussion

Predicate will be evaluated on the media selection option selected for the asset. Media selection options for primary assets may be specified in the AVAssetDownloadConfiguration mediaSelections property. Media selection options for interstitial assets may be circumscribed by -[AVAssetDownloadConfiguration setInterstitialMediaSelectionCriteria: forMediaCharacteristic:].

## Parameters

- `isDownmixAudio`: The RHS value for the value of isDownmixAudio in the predicate equation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(fordownmixaudio:))*