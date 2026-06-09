# perform(_:inZoneWith:)

**Framework**: CloudKit  
**Kind**: method

Searches for records matching a predicate in the specified record zone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+ - Deprecated
- watchOS 8.0+

## Declaration

```swift
func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZone.ID?) async throws -> [CKRecord]
```

#### Discussion

- Returns The records that match the specified query.

For information on a more convenient way to search a database, see [`records(matching:inZoneWith:desiredKeys:resultsLimit:)`](ckdatabase/records(matching:inzonewith:desiredkeys:resultslimit:).md).

## Parameters

- `query`: The query that contains the search parameters. For more information, see [`CKQuery`](ckquery.md).
- `zoneID`: The identifier of the record zone to search. If you’re searching a shared database, provide a record zone identifier; otherwise, you can specify `nil` to search all record zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/perform(_:inzonewith:))*