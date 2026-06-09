# title

**Framework**: Foundation  
**Kind**: property

An optional, user-visible title for this activity, such as a document name or web page title.

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
var title: String? { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)
- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md)

#### Discussion

Always specify a title string for activity objects that are eligible for searches, and it’s recommended that you include a title string for all user activity objects. For search-related user activity objects, this string is displayed in the search results.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/title)*