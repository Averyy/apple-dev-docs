# zones

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

The zones in the database where the changes occurred.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute CloudKit.RecordZoneChangesOptions[] zones;
```

#### Discussion

To fetch record changes in these zones, pass this property to the [`fetchRecordZoneChanges`](../cloudkit.database/fetchrecordzonechanges.md) method in the [`CloudKit.Database`](../cloudkit.database.md) class.

## See Also

### Response Properties
- [moreComing](./morecoming.md)
  A Boolean value that indicates there are more database changes to fetch.
- [syncToken](./synctoken.md)
  A point in the database’s change history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse/zones)*