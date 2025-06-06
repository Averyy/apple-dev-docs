# CSSearchableItemActionType

**Framework**: Core Spotlight  
**Kind**: var

Indicates that the activity type to continue is related to a searchable item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
let CSSearchableItemActionType: String
```

#### Discussion

The `CSSearchableItemActionType` and `CSSearchableItemActivityIdentifier` constants help your app restore state or an activity when a user opens a searchable item listed in a search result. When the user opens the item, Handoff calls your app delegate’s `application(_:willContinueUserActivityWithType:)` method with `CSSearchableItemActionType`. Handoff also delivers an `NSUserActivity` object that contains a `userInfo` dictionary in which the key is `CSSearchableItemActivityIdentifier` and the associated value is the unique identifier that was used when the item was created. Your app delegate can check for the unique identifier in its `application(_:continue:restorationHandler:)` method.

To learn more about enabling Handoff in your app, see the [`Handoff Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338).

## See Also

- [let CSSearchableItemActivityIdentifier: String](cssearchableitemactivityidentifier.md)
  The key you use to access a searchable item in a user activity object.
- [let CSQueryContinuationActionType: String](csquerycontinuationactiontype.md)
  Indicates that the activity type to continue is a search or query.
- [let CSSearchQueryString: String](cssearchquerystring.md)
  Provides the key for the current query in the info dictionary of the user activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemactiontype)*