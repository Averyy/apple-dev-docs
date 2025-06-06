# getZones

**Framework**: CKTool JS  
**Kind**: method

Returns a collection of zones.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise getZones(
	GetZonesParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBZonesResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary GetZonesParams {
  string containerId;
  CKEnvironment environment;
  string databaseType;
  string? continuationToken;
}
```

- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.
- `databaseType`: The database type. For valid values, see `CKDatabaseType`.
- `continuationToken`: Optional continuation token that defines your place in the collection of zones. If the `getZones` response contains a continuation token, you can provide that token here to fetch the next set of zones.

If successful, the returned result contains a `CKDBZonesResponse` object with an array of zones. If there are more zones than the server can return in one response, the server provides a continuation token to fetch the next set of zones.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [createZone](promisesapi/createzone.md)
  Creates a new zone.
- [deleteZone](promisesapi/deletezone.md)
  Deletes a zone.
- [getZone](promisesapi/getzone.md)
  Returns details for a zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/getzones)*