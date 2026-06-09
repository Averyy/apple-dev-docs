# NSUserActivityPersistentIdentifier

**Framework**: Foundation  
**Kind**: typealias

The type that defines a persistent identifier value for an activity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias NSUserActivityPersistentIdentifier = String
```

#### Discussion

In Objective-C, [`NSUserActivity`](nsuseractivity.md) persistent identifiers are a type alias of [`NSString`](nsstring.md). In Swift, [`NSUserActivity`](nsuseractivity.md) persistent identifiers use the [`NSUserActivityPersistentIdentifier`](nsuseractivitypersistentidentifier.md) structure.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitypersistentidentifier)*