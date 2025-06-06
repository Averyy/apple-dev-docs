# CKTool JS

**Framework**: CKTool JS  
**Kind**: module

Manage your CloudKit containers and databases from JavaScript.

**Availability**:
- CKTool JS 1.2.15+

#### Overview

CKTool JS gives you access to features provided in the CloudKit Console API, facilitating CloudKit setup operations for local development and integration testing. It’s a JavaScript client library alternative to the macOS `cktool` command-line utility distributed with Xcode. To learn more about `cktool`, see [`Automating CloudKit Development`](https://developer.apple.comhttps://developer.apple.com/icloud/cloudkit/automating/).

With this library, you can:

- Apply a CloudKit schema file to Sandbox databases (for more information about CloudKit schema files, see [`Integrating a Text-Based Schema into Your Workflow`](https://developer.apple.com/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow)).
- Populate databases with test data.
- Reset Sandbox databases to the production configuration.
- Write scripts for your integration tests to incorporate.

The library consists of three main modules:

- [`CKToolDatabaseModule`](cktooldatabasemodule.md): This package contains all the CloudKit related types and methods, operations to fetch teams and containers for the authorized user, and utility functions and types to communicate with the CloudKit servers. This package also contains operations to work with CloudKit records. You include `@apple/cktool.database` as a dependency in your `package.json` file to access this package.
- [`CKToolNodeJsModule`](cktoolnodejsmodule.md): This package contains a [`createConfiguration`](cktoolnodejsmodule/createconfiguration.md) function you use in projects intended to run in Node.js. You include `@apple/cktool.target.nodejs` as a dependency in your `package.json` file to access this package.
- [`CKToolBrowserModule`](cktoolbrowsermodule.md): This package contains a [`createConfiguration`](cktoolbrowsermodule/createconfiguration.md) function for use in browser-based projects. You include `@apple/cktool.target.browser` as a dependency in your `package.json` file to access this package.

## Topics

### Essentials
- [Integrating CloudKit access into your JavaScript automation scripts](integrating-cloudkit-access-into-your-javascript-automation-scripts.md)
  Configure your JavaScript project to use CKTool JS.
### Promises API
- [PromisesApi](promisesapi.md)
  A class that exposes promise-based functions for interacting with the API.
- [CancellablePromise](cancellablepromise.md)
  A promise that has a function to cancel its operation.
- [CKToolDatabaseModule](cktooldatabasemodule.md)
  The imported package that provides access to CloudKit containers and databases.
### Configuration
- [Configuration](configuration.md)
  An object you use to hold options for communicating with the API server.
- [CKToolNodeJsModule](cktoolnodejsmodule.md)
  The imported package that supports using the client library within a Node.js environment.
- [CKToolBrowserModule](cktoolbrowsermodule.md)
  The imported package that supports using the client library within a web browser.
### Global Structures and Enumerations
- [Container](container.md)
  Details about a CloudKit container.
- [ContainersResponse](containersresponse.md)
  An object that represents results of fetching multiple CloudKit containers.
- [CKEnvironment](ckenvironment.md)
  An enumeration of container environments.
- [ContainersSortByField](containerssortbyfield.md)
  An enumeration that indicates sorting options for retrieved containers.
- [SortDirection](sortdirection.md)
  An enumeration that indicates sorting direction when applying a custom sort.
### Errors
- [ErrorBase](errorbase.md)
  The base class of any error emitted by functions in the client library.
- [Database, Length, Validation, and Value Errors](database-length-validation-and-value-errors.md)
### Classes
- [Blob](blob.md)
- [File](file.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CKToolJS)*