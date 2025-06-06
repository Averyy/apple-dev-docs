# CSQueryContinuationActionType

**Framework**: Core Spotlight  
**Kind**: var

Indicates that the activity type to continue is a search or query.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
let CSQueryContinuationActionType: String
```

#### Discussion

To support search continuation, be sure to include the `CoreSpotlightContinuation` key in your Info.plist file with the value `true`. When users continue a query they started in Spotlight, the system calls your app delegate’s `application(_:willContinueUserActivityWithType:)` method with `CSQueryContinuationActionType`. Then, your app delegate receives an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object that contains a `userInfo` dictionary that includes the [`CSSearchQueryString`](cssearchquerystring.md) key in its `application(_:continue:restorationHandler:)` method. You use the query string associated with this key to continue the search.

## See Also

- [let CSSearchQueryString: String](cssearchquerystring.md)
  Provides the key for the current query in the info dictionary of the user activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csquerycontinuationactiontype)*