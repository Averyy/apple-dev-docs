# CKEnvironment

**Framework**: CKTool JS  
**Kind**: enum

An enumeration of container environments.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKEnvironment {
	const string DEVELOPMENT;
	const string PRODUCTION;
};
```

#### Overview

During initial development of your app, you create your schema and add records for testing in the development environment. Apps sold in the App Store can only access the production environment. Before you publish your app, you must deploy the development schema to the production environment to copy over its record types, fields, and indexes.

```javascript
import { CKEnvironment } from "@apple/cktool.database";
```

## Topics

### Enumeration Cases
- [DEVELOPMENT](ckenvironment/development.md)
- [PRODUCTION](ckenvironment/production.md)

## See Also

- [Container](container.md)
  Details about a CloudKit container.
- [ContainersResponse](containersresponse.md)
  An object that represents results of fetching multiple CloudKit containers.
- [ContainersSortByField](containerssortbyfield.md)
  An enumeration that indicates sorting options for retrieved containers.
- [SortDirection](sortdirection.md)
  An enumeration that indicates sorting direction when applying a custom sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckenvironment)*