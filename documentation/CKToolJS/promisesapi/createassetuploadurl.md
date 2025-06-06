# createAssetUploadUrl

**Framework**: CKTool JS  
**Kind**: method

Creates a new URL for uploading assets.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise createAssetUploadUrl(
	CreateAssetUploadUrlParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 201; result: CKDBAssetUploadUrlResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary CreateAssetUploadUrlParams {
  CKDBCreateAssetUploadUrlRequestBody body;
  string containerId;
  CKEnvironment environment;
  string databaseType;
  string zoneName;
}
```

- `body`: Details of the request to create an asset upload URL.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `databaseType`: The database type. For valid values, see `CKDatabaseType`.
- `zoneName`: The zone name. See `CKDBZone`.

If successful, the result contains the URL to use when uploading an asset, which is valid for 15 minutes. Use this URL to upload your asset and provide the asset fields returned by the upload when creating or updating a record. The following fields are returned if the asset upload is successful: `size`, `receipt`, `fileChecksum`, `wrappingKey`, `referenceChecksum`. You can use these values when creating a `CKDBRecordFieldAssetValue` object for your asset field type.

## Parameters

- `params`: A dictionary as described in the Discussion section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/createassetuploadurl)*