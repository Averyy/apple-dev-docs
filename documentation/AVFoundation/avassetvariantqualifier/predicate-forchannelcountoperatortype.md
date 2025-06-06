# predicate(forChannelCount:operatorType:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 18.5+ (Beta)
- iPadOS 18.5+ (Beta)
- Mac Catalyst 18.5+ (Beta)
- macOS 15.5+ (Beta)
- tvOS 18.5+ (Beta)
- visionOS 2.5+ (Beta)
- watchOS 11.5+ (Beta)

## Declaration

```swift
class func predicate(forChannelCount channelCount: Int, operatorType: NSComparisonPredicate.Operator) -> NSPredicate
```

#### Discussion

```None
			The RHS value for the channel count in the predicate equation.
```

Predicate will be evaluated on the media selection option selected for the asset. Media selection options for primary assets may be specified in the AVAssetDownloadConfiguration 			mediaSelections property. Media selection options for interstitial assets may be circumscribed by -[AVAssetDownloadConfiguration 			setInterstitialMediaSelectionCriteria: forMediaCharacteristic:].

## Parameters

- `operatorType`: The valid values are NSLessThanPredicateOperatorType, NSLessThanOrEqualToPredicateOperatorType, NSGreaterThanPredicateOperatorType, NSGreaterThanOrEqualToPredicateOperatorType, NSEqualToPredicateOperatorType and NSNotEqualToPredicateOperatorType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/predicate(forchannelcount:operatortype:))*