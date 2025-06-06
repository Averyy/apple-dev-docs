# zones

**Framework**: CloudKit JS  
**Kind**: property

The zones in the database where the changes occurred.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute CloudKit.RecordZoneChangesOptions[] zones;
```

#### Discussion

To fetch record changes in these zones, pass this property to the [`fetchRecordZoneChanges`](cloudkit.database/fetchrecordzonechanges.md) method in the [`CloudKit.Database`](cloudkit.database.md) class.

## See Also

- [moreComing](cloudkit.databasechangesresponse/morecoming.md)
  A Boolean value that indicates there are more database changes to fetch.
- [syncToken](cloudkit.databasechangesresponse/synctoken.md)
  A point in the database’s change history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse/zones)*