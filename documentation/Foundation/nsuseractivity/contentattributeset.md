# contentAttributeSet

**Framework**: Foundation  
**Kind**: property

A set of properties that describe the activity.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var contentAttributeSet: CSSearchableItemAttributeSet? { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

A [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) object encapsulates the set of properties you want to display for a searchable activity.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/contentattributeset)*