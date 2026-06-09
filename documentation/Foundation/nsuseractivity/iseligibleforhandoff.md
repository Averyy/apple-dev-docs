# isEligibleForHandoff

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the activity can continue on another device using Handoff.

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
var isEligibleForHandoff: Bool { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

Set the value of this property to `true` for activities you can continue on a person’s other devices; otherwise, set it to `false`. The default value of this property is `true`.

For information about how to support Handoff in your app, see [`Implementing Handoff in Your App`](implementing-handoff-in-your-app.md).

## See Also

- [var isEligibleForSearch: Bool](nsuseractivity/iseligibleforsearch.md)
  A Boolean value that indicates whether to add the activity to the on-device index.
- [var isEligibleForPublicIndexing: Bool](nsuseractivity/iseligibleforpublicindexing.md)
  A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [var isEligibleForPrediction: Bool](nsuseractivity/iseligibleforprediction.md)
  A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [var expirationDate: Date?](nsuseractivity/expirationdate.md)
  The date after which the activity is no longer eligible for Handoff or indexing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforhandoff)*