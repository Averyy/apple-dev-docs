# CSSearchQueryError.Code

**Framework**: Core Spotlight  
**Kind**: enum

Error codes that describe reasons a query might fail.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Getting the error codes.
- [CSSearchQueryError.Code.cancelled](cssearchqueryerror/code/cancelled.md)
  The query stopped because someone canceled it.
- [CSSearchQueryError.Code.indexUnreachable](cssearchqueryerror/code/indexunreachable.md)
  The index is unreachable.
- [CSSearchQueryError.Code.invalidQuery](cssearchqueryerror/code/invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [CSSearchQueryError.Code.unknown](cssearchqueryerror/code/unknown.md)
  An unknown error occurred.
### Creating a query error
- [init?(rawValue: Int)](cssearchqueryerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code)*