# activityType

**Framework**: Foundation  
**Kind**: property

The user activity object’s activity type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var activityType: String { get }
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Discussion

This property is set at initialization time and can’t be changed later. Typically, you specify activity type strings using a reverse-DNS format that uniquely identifies the activity.

## See Also

- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/activitytype)*