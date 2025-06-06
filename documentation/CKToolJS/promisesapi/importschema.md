# importSchema

**Framework**: CKTool JS  
**Kind**: method

Uploads a file that defines the new schema for the container.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise importSchema(
	ImportSchemaParams params
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
dictionary ImportSchemaParams {
  File file;
  string teamId;
  string containerId;
  CKEnvironment environment;
}
```

- `file`:
- `teamId`: The team identifier. You can find your team identifier in the Membership tab of the Apple Developer portal at `https://developer.apple.com`.
- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.

Changes the container’s schema using the uploaded text file for the environment specified. If the operation completes successfully, the server returns a success response. The text you provide in the file object must be in CloudKit Schema Language. To learn more about CloudKit Schema Language, see `https://developer.apple.com/documentation/cloudkit/integrating_a_text-based_schema_into_your_workflow`. Note that in most cases, you use `CKEnvironment.DEVELOPMENT` as the environment. Related: `exportSchema`, `validateSchema`.

Node.js example:

```javascript

import { CKEnvironment, PromisesApi } from "@apple/cktool.database";
import { File, createConfiguration } from "@apple/cktool.target.nodejs";
import fs from "fs/promises";

try {
  const api = new PromisesApi({
    configuration: createConfiguration(),
    security: {
      // You can obtain a management token from the
      // Database section of CloudKit Console.
      "ManagementTokenAuth": "YOUR_MANAGEMENT_TOKEN"
    },
  });

  console.log(`Uploading schema...`);
  // Read a schema file from the file system
  const srcPath = path.join(__dirname, "sample.CKDB");
  const buffer = await fs.readFile(srcPath);
  // Wrap in a File object.
  const file = new File([buffer], "sample.CKDB");
  // Apply the schema to the sandbox.
  await api.importSchema({
    teamId: "YOUR_TEAM_ID",
    containerId: "YOUR_CONTAINER_ID",
    environment: CKEnvironment.DEVELOPMENT,
    file,
  });
  console.log(`Schema uploaded successfully`);
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
- [resetConfigToProduction](promisesapi/resetconfigtoproduction.md)
  Resets the container configuration to production.
- [resetToProduction](promisesapi/resettoproduction.md)
  Resets the schema of the environment to production.
- [validateSchema](promisesapi/validateschema.md)
  Validates the uploaded schema file for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/importschema)*