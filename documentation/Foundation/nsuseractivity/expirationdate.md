# expirationDate

**Framework**: Foundation  
**Kind**: property

The date after which the activity is no longer eligible for Handoff or indexing.

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
var expirationDate: Date? { get set }
```

#### Discussion

If you don’t set the value of this property, the system automatically expires the activity after a period of time.

## See Also

- [var isEligibleForHandoff: Bool](nsuseractivity/iseligibleforhandoff.md)
  A Boolean value that indicates whether the activity can be continued on another device using Handoff.
- [var isEligibleForSearch: Bool](nsuseractivity/iseligibleforsearch.md)
  A Boolean value that indicates whether the activity should be added to the on-device index.
- [var isEligibleForPublicIndexing: Bool](nsuseractivity/iseligibleforpublicindexing.md)
  A Boolean value that indicates whether the activity can be publicly accessed by all iOS users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/expirationdate)*