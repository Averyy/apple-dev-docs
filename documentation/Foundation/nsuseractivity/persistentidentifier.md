# persistentIdentifier

**Framework**: Foundation  
**Kind**: property

A unique and persistent value you use to identify the activity.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var persistentIdentifier: NSUserActivityPersistentIdentifier? { get set }
```

## Mentions

- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md)

#### Discussion

Set this property to a value that identifies the user activity so you can later delete it with [`deleteSavedUserActivities(withPersistentIdentifiers:completionHandler:)`](nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:).md). For example, if the user checks the weather for Cupertino each morning from home, the weather app sets the persistent identifier to the city name (Cupertino). When the user deletes Cupertino from the weather app, the app deletes the user activity associated with the identifier, “Cupertino”.

```swift
let userActivity = NSUserActivity(activityType: WeatherLookup.userActivityType)
userActivity.persistentIdentifier = "Cupertino"
```

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/persistentidentifier)*