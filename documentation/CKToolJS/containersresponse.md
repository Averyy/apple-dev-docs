# ContainersResponse

**Framework**: CKTool JS  
**Kind**: struct

An object that represents results of fetching multiple CloudKit containers.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary ContainersResponse {
	string? nextKey;
	string? previousKey;
	Container[] containers;
	Container[]? recentContainers;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { ContainersResponse } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [containers](containersresponse/containers.md)
  The list of containers.
- [nextKey](containersresponse/nextkey.md)
  The record key for fetching the next page of results.
- [previousKey](containersresponse/previouskey.md)
  The record key for fetching the previous page of results.
- [recentContainers](containersresponse/recentcontainers.md)
  The list of recently accessed containers.

## See Also

- [Container](container.md)
  Details about a CloudKit container.
- [CKEnvironment](ckenvironment.md)
  An enumeration of container environments.
- [ContainersSortByField](containerssortbyfield.md)
  An enumeration that indicates sorting options for retrieved containers.
- [SortDirection](sortdirection.md)
  An enumeration that indicates sorting direction when applying a custom sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/containersresponse)*