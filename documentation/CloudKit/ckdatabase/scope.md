# CKDatabase.Scope

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the scope of a database.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Scope
```

```c
enum CKDatabaseScope : NSInteger;
```

## Topics

### Database Scopes
- [CKDatabase.Scope.public](./scope/public.md)
  The public database.
- [CKDatabase.Scope.private](./scope/private.md)
  The private database.
- [CKDatabase.Scope.shared](./scope/shared.md)
  The shared database.
### Initializers
- [init?(rawValue: Int)](./scope/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Database Type
- [var databaseScope: CKDatabase.Scope](./databasescope.md)
  The type of database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope)*