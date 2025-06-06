# CSSearchQueryError.Code.cancelled

**Framework**: Core Spotlight  
**Kind**: case

The query stopped because someone canceled it.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
case cancelled
```

#### Discussion

The system reports this error if your code called the [`cancel()`](csuserquery/cancel().md) method.

## See Also

- [CSSearchQueryError.Code.indexUnreachable](cssearchqueryerror/code/indexunreachable.md)
  The index is unreachable.
- [CSSearchQueryError.Code.invalidQuery](cssearchqueryerror/code/invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [CSSearchQueryError.Code.unknown](cssearchqueryerror/code/unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/cancelled)*