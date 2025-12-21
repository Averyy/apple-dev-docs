# MigrationStatus.failure(_:)

**Framework**: AppMigrationKit  
**Kind**: case

The migration failed with an error.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case failure(any Error)
```

#### Discussion

Inspect the associated value to retrieve the [`Error`](https://developer.apple.com/documentation/Swift/Error) that caused migration to fail.

## See Also

- [MigrationStatus.success](migrationstatus/success.md)
  The migration completed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/failure(_:))*