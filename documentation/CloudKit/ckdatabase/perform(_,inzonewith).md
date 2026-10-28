# perform(_:inZoneWith:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Searches for records matching a predicate in the specified record zone.

**Availability**:
- iOS 15.0+ - Deprecated in 15.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- iPadOS 15.0+ - Deprecated in 15.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- Mac Catalyst 15.0+ - Deprecated in 15.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- macOS 12.0+ - Deprecated in 12.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- tvOS 15.0+ - Deprecated in 15.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- visionOS - Deprecated (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))
- watchOS 8.0+ - Deprecated in 8.0 (renamed: CKDatabase.records(matching:inZoneWith:desiredKeys:resultsLimit:))

## Declaration

```swift
func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZone.ID?) async throws -> [CKRecord]
```

## Return Value

The records that match the specified query.

## Discussion

For information on a more convenient way to search a database, see [`records(matching:inZoneWith:desiredKeys:resultsLimit:)`](./records%28matching,inzonewith,desiredkeys,resultslimit%29.md).

## Parameters

- `query`: The query that contains the search parameters. For more information, see [`CKQuery`](../ckquery.md).
- `zoneID`: The identifier of the record zone to search. If you’re searching a shared database, provide a record zone identifier; otherwise, you can specify `nil` to search all record zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/perform(_:inzonewith:))*