# CSSearchableItemActivityIdentifier

**Framework**: Core Spotlight  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const CSSearchableItemActivityIdentifier;
```

#### Discussion

Use this key to access the unique identifier for the searchable item from the [`userInfo`](../Foundation/nsuseractivity/userinfo.md) dictionary of a [`NSUserActivity`](../Foundation/nsuseractivity.md) object.

## See Also

### Continuing a search or activity
- [let CSSearchableItemActionType: String](./cssearchableitemactiontype.md)
  Indicates that the activity type to continue is related to a searchable item.
- [let CSQueryContinuationActionType: String](./csquerycontinuationactiontype.md)
  Indicates that the activity type to continue is a search or query.
- [let CSSearchQueryString: String](./cssearchquerystring.md)
  Provides the key for the current query in the info dictionary of the user activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemactivityidentifier)*