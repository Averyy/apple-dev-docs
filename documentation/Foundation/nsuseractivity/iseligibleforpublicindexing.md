# isEligibleForPublicIndexing

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the activity can be publicly accessed by all iOS users.

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
var isEligibleForPublicIndexing: Bool { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), which indicates that the activity object contains private or sensitive information or that the activity isn’t useful to other users. When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system identifies this activity as one that can be shared publicly. When you make an activity public, the system indexes the values in the [`requiredUserInfoKeys`](nsuseractivity/requireduserinfokeys.md) or [`webpageURL`](nsuseractivity/webpageurl.md) properties, and you must provide a value for one of those properties.

Identifying an activity as public confers an advantage when you also add web markup to the content on your related website. Specifically, when users engage with your app’s public activities in search results, it indicates to Apple that public information on your website is popular, which can help increase your ranking and potentially lead to expanded indexing of your website’s content.

## See Also

- [var isEligibleForHandoff: Bool](nsuseractivity/iseligibleforhandoff.md)
  A Boolean value that indicates whether the activity can be continued on another device using Handoff.
- [var isEligibleForSearch: Bool](nsuseractivity/iseligibleforsearch.md)
  A Boolean value that indicates whether the activity should be added to the on-device index.
- [var expirationDate: Date?](nsuseractivity/expirationdate.md)
  The date after which the activity is no longer eligible for Handoff or indexing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforpublicindexing)*