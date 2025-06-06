# fetchDatabaseChanges

**Framework**: CloudKit JS  
**Kind**: method

Fetch changed record zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.DatabaseChangesResponse, CKError> fetchDatabaseChanges(
	optional Object options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.DatabaseChangesResponse`](cloudkit.databasechangesresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

For example, use this method to fetch the zones that changed and then use the [`fetchRecordZoneChanges`](cloudkit.database/fetchrecordzonechanges.md) method to fetch the changed records in each zone.

```javascript
database.fetchDatabaseChanges().then(function(response) {
   return database.fetchRecordZoneChanges(response.zones)
})
.then(function(response) {
   response.zones.forEach(function(zone) {
       zone.records.forEach(function(record) {
          // Apply the record change
       })
   })
})
```

## Parameters

- `options`: Options to fetch database changes. This   object has one key:

## See Also

- [databaseScope](cloudkit.database/databasescope.md)
  The type of database (public, private, or shared).
- [fetchRecordZoneChanges](cloudkit.database/fetchrecordzonechanges.md)
  Fetch changes to the specified record zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchdatabasechanges)*