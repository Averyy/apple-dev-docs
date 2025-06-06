# Integrating CloudKit access into your JavaScript automation scripts

**Framework**: CKTool JS

Configure your JavaScript project to use CKTool JS.

#### Overview

Include CKTool JS in your JavaScript automation testing and continuous integration tasks to manipulate the schema and the data in your database. To start using CKTool JS in your scripts, you need to:

- Generate a CloudKit management token
- Install CKTool JS and configure it for your environment
- Initialize the database API for your scripts to use

##### Obtain a Cloudkit Management Token

CKTool JS requires a CloudKit management token from the CloudKit Console within the [`Apple Developer Portal`](https://developer.apple.comhttps://developer.apple.com). Generate the token from the CloudKit Console by choosing the Settings section for your account. Save this token, because it won’t be visible again.

If you’ll be accessing with data in a container, then you’ll also require a user token. You can obtain a user token from CloudKit Console.

##### Specify and Install the Cktool Js Packages

To install the CKTool JS client library, you need to have the `npm` package management tool already installed on your machine. The client library suite includes a main database package and a package used to target Node.js.

> **Note**:  Each package includes TypeScript type definitions, which enable static type checking and code completion while editing your code.

 Each package includes TypeScript type definitions, which enable static type checking and code completion while editing your code.

Add the CKTool JS database package to your `package.json`, alongside any other runtime dependencies that you may have.

```javascript
{
  "dependencies": {
    "@apple/cktool.database": "^1.3.2",
    "@apple/cktool.target.nodejs": "^1.3.2",
    ...
  },
  ...
}
```

Now that you’ve specified your additional `package.json` dependencies, install them. Run the following command in your project directory.

```other
$ npm install
```

This command downloads the CKTool JS packages specified in your dependencies.

##### Prepare the Client Library for Use in Your Scripts

In your code, import the configuration factory function for Node.js. This prepares a configuration object for your target platform that the client library requires for initialization.

```javascript
import { createConfiguration } from "@apple/cktool.target.nodejs";
```

After importing the `createConfiguration` function, you instantiate `PromisesApi`, passing the `configuration` instance along with the management token that you generated from CloudKit Console.

```javascript
// Place additional imports at the top.
import { PromisesApi } from "@apple/cktool.database";

const api = new PromisesApi({
  configuration: createConfiguration(),
  security: { "ManagementTokenAuth": "YOUR_MANAGEMENT_TOKEN" }
});

```

Use the [`PromisesApi`](promisesapi.md) instance to access your containers from your scripts.

##### Create a Default Parameters Object to Provide Required Parameters

Most methods on the API object require `teamId`, `containerId`, and `environment`. Each method on the API object takes a single parameters dictionary to pass required and optional values to the method.

If you create a plain JavaScript object to hold these frequently required parameters, you can use the JavaScript object spread operator to create a parameter dictionary to pass to a method.

```javascript
const defaultParams = {
  teamId: "YOUR_TEAM_ID",
  containerId: "YOUR_CONTAINER_ID",
  environment: CKEnvironment.DEVELOPMENT
};
```

The following code shows how you call an API object method with your parameters object.

```javascript
const response = await api.importSchema({
  ...defaultParams,
  file: yourFile,
});
```

In the above example, `importSchema` requires a `file` value as well as the values held in `defaultParams`. Using the object spread syntax copies all of the values from `defaultParams` along with the `file` parameter for you to pass it to `importSchema`.

> **Note**:  You can add additional values to your parameters object. If the method doesn’t use them, it ignores those values.

 You can add additional values to your parameters object. If the method doesn’t use them, it ignores those values.

##### Convert Value Types Into the Librarys Expected Types

In order to pass values to CKTool JS functions that expect `Float`, `Double`, `Int32`, `Int64`, `Byte`, `ByteArray`, or `UUID` values, you must convert the parameters into the appropriate type.

For example, `createCKDBRecordFieldInt64Value` expects a value that’s an `Int64`. To use that function, first convert the value to the expected type using the `toInt64` function.

```javascript
import { toInt64 } from "@apple/cktool.database";
const int64Field = createCKDBRecordFieldInt64Value({
  value: toInt64(123)
});
```

In TypeScript, the compiler catches attempts to pass values of the wrong type. If the value types are mismatched, JavaScript throws a runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/integrating-cloudkit-access-into-your-javascript-automation-scripts)*