# cancelMigrationWithError(_:)

**Framework**: Core Data  
**Kind**: method

Cancels the migration with a given error.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancelMigrationWithError(_ error: any Error)
```

#### Discussion

You can invoke this method from anywhere in the migration process to abort the migration. Calling this method causes [`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`](nsmigrationmanager/migratestore(from:sourcetype:options:with:todestinationurl:destinationtype:destinationoptions:).md) to abort the migration and return `error`—you should provide an appropriate error to indicate the reason for the cancellation.

## Parameters

- `error`: An error object that describes the reason why the migration is canceled.

## See Also

- [func reset()](nsmigrationmanager/reset.md)
  Resets the association tables for the migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/cancelmigrationwitherror(_:))*