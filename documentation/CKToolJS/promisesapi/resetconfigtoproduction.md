# resetConfigToProduction

**Framework**: CKTool JS  
**Kind**: method

Resets the container configuration to production.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise resetConfigToProduction(
	ResetConfigToProductionParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 202 }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary ResetConfigToProductionParams {
  string teamId;
  string containerId;
}
```

- `teamId`: The team identifier. You can find your team identifier in the Membership tab of the Apple Developer portal at `https://developer.apple.com`.
- `containerId`: The container identifier. See `Container`.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [exportSchema](promisesapi/exportschema.md)
  Downloads the container’s schema.
- [getContainers](promisesapi/getcontainers.md)
  Fetches containers for a team.
- [importSchema](promisesapi/importschema.md)
  Uploads a file that defines the new schema for the container.
- [resetToProduction](promisesapi/resettoproduction.md)
  Resets the schema of the environment to production.
- [validateSchema](promisesapi/validateschema.md)
  Validates the uploaded schema file for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/resetconfigtoproduction)*