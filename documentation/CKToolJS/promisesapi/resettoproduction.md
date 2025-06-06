# resetToProduction

**Framework**: CKTool JS  
**Kind**: method

Resets the schema of the environment to production.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise resetToProduction(
	ResetToProductionParams params
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
dictionary ResetToProductionParams {
  string teamId;
  string containerId;
  CKEnvironment environment;
}
```

- `teamId`: The team identifier. You can find your team identifier in the Membership tab of the Apple Developer portal at `https://developer.apple.com`.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.

Changes the schema of the container within the given environment to production and resets the environment. If the operation completes successfully, the server returns a success response.

Node.js example:

```javascript

import { CKEnvironment, PromisesApi } from "@apple/cktool.database";
import { createConfiguration } from "@apple/cktool.target.nodejs";

try {
  const api = new PromisesApi({
    configuration: createConfiguration(),
    security: {
      // You can obtain a management token from the
      // Database section of CloudKit Console.
      "ManagementTokenAuth": "YOUR_MANAGEMENT_TOKEN"
    },
  });

  console.log(`Resetting schema to production...`);
  await api.resetToProduction({
    teamId: "YOUR_TEAM_ID",
    containerId: "YOUR_CONTAINER_ID",
    environment: CKEnvironment.DEVELOPMENT
  });
  console.log(`Schema reset successfully`);
} catch(ex) {
  // Handle error
}
```

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [exportSchema](promisesapi/exportschema.md)
  Downloads the container’s schema.
- [getContainers](promisesapi/getcontainers.md)
  Fetches containers for a team.
- [importSchema](promisesapi/importschema.md)
  Uploads a file that defines the new schema for the container.
- [resetConfigToProduction](promisesapi/resetconfigtoproduction.md)
  Resets the container configuration to production.
- [validateSchema](promisesapi/validateschema.md)
  Validates the uploaded schema file for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/resettoproduction)*