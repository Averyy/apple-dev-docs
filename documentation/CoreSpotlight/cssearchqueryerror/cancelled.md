# cancelled

**Framework**: Core Spotlight  
**Kind**: property

The query stopped because someone canceled it.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
static var cancelled: CSSearchQueryError.Code { get }
```

#### Discussion

The system reports this error if your code called the [`cancel()`](csuserquery/cancel().md) method.

## See Also

- [static var indexUnreachable: CSSearchQueryError.Code](cssearchqueryerror/indexunreachable.md)
  The index is unreachable.
- [static var invalidQuery: CSSearchQueryError.Code](cssearchqueryerror/invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [static var unknown: CSSearchQueryError.Code](cssearchqueryerror/unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/cancelled)*