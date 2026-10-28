# MigrationStatus.failure(_:)

**Framework**: AppMigrationKit  
**Kind**: case  
**Role**: Case

The migration failed with an error.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case failure(any Error)
```

## Discussion

Inspect the associated value to retrieve the [`Error`](../../Swift/error.md) that caused migration to fail.

## See Also

### Examining migration statuses
- [MigrationStatus.success](./success.md)
  The migration completed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/failure(_:))*