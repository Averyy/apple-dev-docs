# CSSearchQueryError.Code.cancelled

**Framework**: Core Spotlight  
**Kind**: case  
**Role**: Case

The query stopped because someone canceled it.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
case cancelled
```

```c
CSSearchQueryErrorCodeCancelled
```

#### Discussion

The system reports this error if your code called the [`cancel()`](../../csuserquery/cancel%28%29.md) method.

## See Also

### Getting the error codes
- [CSSearchQueryError.Code.indexUnreachable](./indexunreachable.md)
  The index is unreachable.
- [CSSearchQueryError.Code.invalidQuery](./invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [CSSearchQueryError.Code.unknown](./unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/cancelled)*