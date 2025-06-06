# queryRecords

**Framework**: CKTool JS  
**Kind**: method

Returns a collection of records matching the provided query.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise queryRecords(
	QueryRecordsParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBRecordsResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary QueryRecordsParams {
  CKDBQueryRecordsRequestBody body;
  string containerId;
  CKEnvironment environment;
  string databaseType;
  string zoneName;
}
```

- `body`: Details of the query to use when fetching records.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `databaseType`: The database type. For valid values, see `CKDatabaseType`.
- `zoneName`: The zone name. See `CKDBZone`.

If successful, the response contains a `CKDBRecordsResponse` object with an array of records. For details on the body parameter see `CKDBQueryRecordsRequestBody`.

Node.js example:

```javascript

import { createConfiguration } from "@apple/cktool.target.nodejs";

import {
  CKDatabaseType,
  CKEnvironment,
  CKDBQueryFilterType,
  PromisesApi,
  createCKDBRecordFieldInt64Value,
  toInt64
} from "@apple/cktool.database";

// These parameters are commonly passed to
// operations on records.
const defaultParams = {
  containerId: "YOUR_CONTAINER_ID",
  environment: CKEnvironment.DEVELOPMENT,
  databaseType: CKDatabaseType.PUBLIC,
  zoneName: "_defaultZone",
};

try {
  const api = new PromisesApi({
    configuration: createConfiguration(),
    security: {
      // You can obtain tokens from CloudKit Console.
      "ManagementTokenAuth": "YOUR_MANAGEMENT_TOKEN",
      "UserTokenAuth": "YOUR_USER_TOKEN"
    },
  });
  const { result } = await api.queryRecords({
    ...defaultParams,
    body: {
      query: {
        recordType: "MyUserAccounts",
        filters: [{
          fieldName: "age",
          type: CKDBQueryFilterType.EQUALS,
          fieldValue: createCKDBRecordFieldInt64Value({
            value: toInt64(42)
          }) 
        }]
      }
    }
  });
  // Do something with result.records
  result.records.forEach((record) => {
    console.log(record.recordName);
  });
  // Optionally use result.continuationToken to
  // fetch more records, if present.
} catch(ex) {
  // Handle error
}
```

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
- [lookupRecords](promisesapi/lookuprecords.md)
  Fetches multiple records by record name.
- [queryRecordChanges](promisesapi/queryrecordchanges.md)
  Returns records that changed since a specified sync token or since a zone was created.
- [resolveRecord](promisesapi/resolverecord.md)
  Fetches information about records given their shortGuid properties.
- [updateRecord](promisesapi/updaterecord.md)
  Updates an existing record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/queryrecords)*