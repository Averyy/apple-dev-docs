# CSSearchQueryError

**Framework**: Core Spotlight  
**Kind**: struct

Search query errors returned by Core Spotlight.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
struct CSSearchQueryError
```

## Topics

### Getting the error codes
- [static var cancelled: CSSearchQueryError.Code](cssearchqueryerror/cancelled.md)
  The query stopped because someone canceled it.
- [static var indexUnreachable: CSSearchQueryError.Code](cssearchqueryerror/indexunreachable.md)
  The index is unreachable.
- [static var invalidQuery: CSSearchQueryError.Code](cssearchqueryerror/invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [static var unknown: CSSearchQueryError.Code](cssearchqueryerror/unknown.md)
  An unknown error occurred.
### Getting codes for query-related errors
- [CSSearchQueryError.Code](cssearchqueryerror/code.md)
  Error codes that describe reasons a query might fail.
### Getting the error description
- [static var errorDomain: String](cssearchqueryerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CSIndexError](csindexerror.md)
  Index errors returned by Core Spotlight.
- [CSIndex Errors](csindex-errors.md)
  Index error codes and error domain.
- [CSSearchQuery Errors](cssearchquery-errors.md)
  Search query error codes and error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror)*