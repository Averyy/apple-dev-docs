# keywords

**Framework**: Foundation  
**Kind**: property

A set of localized keywords that can help users find the activity in search results.

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
var keywords: Set<String> { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

The default value of this property is `nil`. The system indexes the keywords you provide.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/keywords)*