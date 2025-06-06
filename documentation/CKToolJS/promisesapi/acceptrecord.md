# acceptRecord

**Framework**: CKTool JS  
**Kind**: method

Accepts a share on behalf of the current user.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise acceptRecord(
	AcceptRecordParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBResolveRecordResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary AcceptRecordParams {
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

If successful, the result contains a `CKDBResolveRecordResponse` object that contains the resolved record. The recipient must accept the shared record before adding it to their shared database. A shared record’s participants are listed in the `participants` field on `CKDBRecord`. You can update this array using the `updateRecord` operation.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [createRecord](promisesapi/createrecord.md)
  Creates a new record.
- [deleteRecord](promisesapi/deleterecord.md)
  Deletes a single record.
- [deleteRecordsByQuery](promisesapi/deleterecordsbyquery.md)
  Deletes records matching the provided query.
- [getRecord](promisesapi/getrecord.md)
  Returns a record’s details.
- [lookupRecords](promisesapi/lookuprecords.md)
  Fetches multiple records by record name.
- [queryRecordChanges](promisesapi/queryrecordchanges.md)
  Returns records that changed since a specified sync token or since a zone was created.
- [queryRecords](promisesapi/queryrecords.md)
  Returns a collection of records matching the provided query.
- [resolveRecord](promisesapi/resolverecord.md)
  Fetches information about records given their shortGuid properties.
- [updateRecord](promisesapi/updaterecord.md)
  Updates an existing record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/acceptrecord)*