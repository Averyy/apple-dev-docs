# CSSearchableItemActivityIdentifier

**Framework**: Core Spotlight  
**Kind**: var

The key you use to access a searchable item in a user activity object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
let CSSearchableItemActivityIdentifier: String
```

#### Discussion

Use this key to access the unique identifier for the searchable item from the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary of a [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object.

## See Also

- [let CSSearchableItemActionType: String](cssearchableitemactiontype.md)
  Indicates that the activity type to continue is related to a searchable item.
- [let CSQueryContinuationActionType: String](csquerycontinuationactiontype.md)
  Indicates that the activity type to continue is a search or query.
- [let CSSearchQueryString: String](cssearchquerystring.md)
  Provides the key for the current query in the info dictionary of the user activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemactivityidentifier)*