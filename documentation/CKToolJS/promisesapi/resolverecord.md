# resolveRecord

**Framework**: CKTool JS  
**Kind**: method  
**Role**: Instance Method

Fetches information about records given their shortGuid properties.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
CancellablePromise resolveRecord(
	ResolveRecordParams params
);
```

## Return Value

A `CancellablePromise` with the following resolutions.

## Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBResolveRecordResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

## Discussion

The `params` dictionary has the following properties:

```javascript
dictionary ResolveRecordParams {
  string containerId;
  CKEnvironment environment;
  string shortGuid;
  CKDBResolveRecordRequestBody? body;
}
```

- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `shortGuid`: A global unique identifier for this record used for sharing. See `createRecord` for information on retrieving this identifier.
- `body`: Configuration options for how the resolved record is returned.

If successful, the response contains a `CKDBResolveRecordResponse` object with the resolved record.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

### Record Management
- [acceptRecord](./acceptrecord.md)
  Accepts a share on behalf of the current user.
- [createRecord](./createrecord.md)
  Creates a new record.
- [deleteRecord](./deleterecord.md)
  Deletes a single record.
- [deleteRecordsByQuery](./deleterecordsbyquery.md)
  Deletes records matching the provided query.
- [getRecord](./getrecord.md)
  Returns a record’s details.
- [lookupRecords](./lookuprecords.md)
  Fetches multiple records by record name.
- [queryRecordChanges](./queryrecordchanges.md)
  Returns records that changed since a specified sync token or since a zone was created.
- [queryRecords](./queryrecords.md)
  Returns a collection of records matching the provided query.
- [updateRecord](./updaterecord.md)
  Updates an existing record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/resolverecord)*