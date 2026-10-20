# invalidQuery

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Type Property

The query is syntactically invalid or specifies items that your app doesn’t have access to.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
static var invalidQuery: CSSearchQueryError.Code { get }
```

## See Also

### Getting the error codes
- [static var cancelled: CSSearchQueryError.Code](./cancelled.md)
  The query stopped because someone canceled it.
- [static var indexUnreachable: CSSearchQueryError.Code](./indexunreachable.md)
  The index is unreachable.
- [static var unknown: CSSearchQueryError.Code](./unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/invalidquery)*