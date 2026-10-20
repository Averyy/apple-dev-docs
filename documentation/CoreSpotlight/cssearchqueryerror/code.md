# CSSearchQueryError.Code

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

Error codes that describe reasons a query might fail.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum CSSearchQueryErrorCode : NSInteger;
```

## Topics

### Getting the error codes
- [CSSearchQueryError.Code.cancelled](./code/cancelled.md)
  The query stopped because someone canceled it.
- [CSSearchQueryError.Code.indexUnreachable](./code/indexunreachable.md)
  The index is unreachable.
- [CSSearchQueryError.Code.invalidQuery](./code/invalidquery.md)
  The query is syntactically invalid or specifies items that your app doesn’t have access to.
- [CSSearchQueryError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
### Creating a query error
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code)*