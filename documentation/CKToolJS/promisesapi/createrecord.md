# createRecord

**Framework**: CKTool JS  
**Kind**: method

Creates a new record.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise createRecord(
	CreateRecordParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 201; result: CKDBRecordResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary CreateRecordParams {
  CKDBCreateRecordRequestBody body;
  string containerId;
  CKEnvironment environment;
  string databaseType;
  string zoneName;
}
```

- `body`: New record details.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `databaseType`: The database type. For valid values, see `CKDatabaseType`.
- `zoneName`: The zone name. See `CKDBZone`.

If successful, the result contains a `CKDBRecordResponse` object with the created record. When creating a new record, if you omit the `recordName` property from `body`, the server assigns the record a UUID. When `assetType` fields exist in your record type, you must upload the assets prior to creating a record using the `createAssetUploadUrl` operation. For shared records, set the `createShortGuid` property in `body` to `true` in order to create a globally unique identifier for this record that the server uses when the share participant accepts a shared record.

Node.js example:

```javascript

import { createConfiguration } from "@apple/cktool.target.nodejs";
import {
  CKDatabaseType,
  CKEnvironment,
  PromisesApi,
  createCKDBRecordFieldInt64Value,
  createCKDBRecordFieldStringValue,
  createCKDBRecordFieldStringListValue,
  createCKDBRecordFieldTimestampValue,
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
  const { result } = await api.createRecord({
    ...defaultParams,
    body: {
      recordType: "MyUserAccounts",
      fields: {
        "firstName": createCKDBRecordFieldStringValue({ value: "John" }),
        "lastName": createCKDBRecordFieldStringValue({ value: "Smith" }),
        "age": createCKDBRecordFieldInt64Value({
          // toInt64 casts the number to an Int64
          value: toInt64(42)
        }),
        "dateOfBirth": createCKDBRecordFieldTimestampValue({
          value: new Date("Mar 4, 1979")
        }),
        "childrenNames": createCKDBRecordFieldStringListValue({
          value: ["Fred", "Bob"]
        })
      }
    }
  });
  // Do something with result.record
  console.log(result.record.recordName);
} catch(ex) {
  // Handle error
}
```

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [acceptRecord](promisesapi/acceptrecord.md)
  Accepts a share on behalf of the current user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/createrecord)*