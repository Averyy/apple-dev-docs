# lookupRecords

**Framework**: CKTool JS  
**Kind**: method

Fetches multiple records by record name.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise lookupRecords(
	LookupRecordsParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBLookupRecordsResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary LookupRecordsParams {
  CKDBLookupRecordsRequestBody body;
  string containerId;
  CKEnvironment environment;
  string databaseType;
  string zoneName;
}
```

- `body`: The array of record names to look up.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `databaseType`: The database type. For valid values, see `CKDatabaseType`.
- `zoneName`: The zone name. See `CKDBZone`.

If successful, the server returns a `CKDBLookupRecordsResponse` object, which contains an array of `CKDBRecordResult` objects. `CKDBRecordResult` can represent three types of records: existing, deleted, and error. You can verify that a returned record isn’t missing or deleted by checking that the type is set to `existing`.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [acceptRecord](promisesapi/acceptrecord.md)
  Accepts a share on behalf of the current user.
- [createRecord](promisesapi/createrecord.md)
  Creates a new record.
- [deleteRecord](promisesapi/deleterecord.md)
  Deletes a single record.
- [deleteRecordsByQuery](promisesapi/deleterecordsbyquery.md)
  Deletes records matching the provided query.
- [getRecord](promisesapi/getrecord.md)
  Returns a record’s details.
- [queryRecordChanges](promisesapi/queryrecordchanges.md)
  Returns records that changed since a specified sync token or since a zone was created.
- [queryRecords](promisesapi/queryrecords.md)
  Returns a collection of records matching the provided query.
- [resolveRecord](promisesapi/resolverecord.md)
  Fetches information about records given their shortGuid properties.
- [updateRecord](promisesapi/updaterecord.md)
  Updates an existing record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/lookuprecords)*