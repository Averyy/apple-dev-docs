# exportSchema

**Framework**: CKTool JS  
**Kind**: method

Downloads the container’s schema.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise exportSchema(
	ExportSchemaParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: Blob }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary ExportSchemaParams {
  string teamId;
  string containerId;
  CKEnvironment environment;
}
```

- `teamId`: The team identifier. You can find your team identifier in the Membership tab of the Apple Developer portal at `https://developer.apple.com`.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.

Downloads a schema file for the environment specified. If the operation completes successfully, the returned response contains the textual representation of the container’s schema for the given environment. The text obtained this way is in CloudKit Schema Language. To learn more about CloudKit Schema Language, see `https://developer.apple.com/documentation/cloudkit/integrating_a_text-based_schema_into_your_workflow`. Related: `importSchema`, `validateSchema`.

Node.js example:

```javascript

import { CKEnvironment, PromisesApi } from "@apple/cktool.database";
import { createConfiguration } from "@apple/cktool.target.nodejs";
import fs from "fs/promises";
import path from "path";

try {
  const api = new PromisesApi({
    configuration: createConfiguration(),
    security: {
      // You can obtain a management token from the
      // Database section of CloudKit Console.
      "ManagementTokenAuth": "YOUR_MANAGEMENT_TOKEN"
    },
  });

  console.log(`Downloading schema...`);
  const response = await api.exportSchema({
    teamId: "YOUR_TEAM_ID",
    containerId: "YOUR_CONTAINER_ID",
    environment: CKEnvironment.DEVELOPMENT
  });
  const destPath = path.default.join(__dirname, "sample.CKDB");
  const arrayBuffer = await response.result.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);
  await fs.default.writeFile(destPath, buffer);
  console.log(`Schema downloaded to ${destPath}`);
} catch (ex) {
  console.error(configuration.jsonStringify(ex));
}
```

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [getContainers](promisesapi/getcontainers.md)
  Fetches containers for a team.
- [importSchema](promisesapi/importschema.md)
  Uploads a file that defines the new schema for the container.
- [resetConfigToProduction](promisesapi/resetconfigtoproduction.md)
  Resets the container configuration to production.
- [resetToProduction](promisesapi/resettoproduction.md)
  Resets the schema of the environment to production.
- [validateSchema](promisesapi/validateschema.md)
  Validates the uploaded schema file for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/exportschema)*