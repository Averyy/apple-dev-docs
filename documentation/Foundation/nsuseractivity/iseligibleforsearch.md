# isEligibleForSearch

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to add the activity to the on-device index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isEligibleForSearch: Bool { get set }
```

```objc
@property (getter=isEligibleForSearch) BOOL eligibleForSearch;
```

## Mentions

- [Creating a user activity object](../creating-a-user-activity-object.md)

## Discussion

If you aren’t yet using App Intents and want to add your user activity objects to the Spotlight indexes, set the value in this property to `true`. When this property is `true` and the user activity object is current, Spotlight indexes the activity so it can appear in search results. Set this property to `false` if you are already indexing [`AppEntity`](../../AppIntents/appentity.md) types or don’t want Spotlight to include someone’s activity-related information in search results. The default value of this property is `false`.

Add an activity object to the search index if it contains information a person might reasonably search for later. For example, a restaurant finder app might index activity objects for each restaurant the person views. Subsequent searches for restaurants using Spotlight can then include the restaurants from your activity objects in the results. Index activity objects only to reflect the content that people touch in your app, not as a substitute for indexing your app’s content using Spotlight.

> ❗ **Important**: Your app must maintain a strong reference to any activity objects you make eligible for search.

## See Also

### Enabling system behaviors
- [var isEligibleForHandoff: Bool](./iseligibleforhandoff.md)
  A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [var isEligibleForPublicIndexing: Bool](./iseligibleforpublicindexing.md)
  A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [var isEligibleForPrediction: Bool](./iseligibleforprediction.md)
  A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [var expirationDate: Date?](./expirationdate.md)
  The date after which the activity is no longer eligible for Handoff or indexing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforsearch)*