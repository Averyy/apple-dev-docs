# predicate(forChannelCount:operatorType:)

**Framework**: AVFoundation  
**Kind**: method

Creates a NSPredicate for audio channel count which can be used with other NSPredicates to express variant preferences.

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
class func predicate(forChannelCount channelCount: Int, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

#### Discussion

Predicate will be evaluated on the media selection option selected for the asset. Media selection options for primary assets may be specified in the AVAssetDownloadConfiguration mediaSelections property. Media selection options for interstitial assets may be circumscribed by -[AVAssetDownloadConfiguration setInterstitialMediaSelectionCriteria: forMediaCharacteristic:].

## Parameters

- `channelCount`: The RHS value for the channel count in the predicate equation.
- `operatorType`: The valid values are NSLessThanPredicateOperatorType, NSLessThanOrEqualToPredicateOperatorType, NSGreaterThanPredicateOperatorType, NSGreaterThanOrEqualToPredicateOperatorType, NSEqualToPredicateOperatorType and NSNotEqualToPredicateOperatorType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forchannelcount:operatortype:))*