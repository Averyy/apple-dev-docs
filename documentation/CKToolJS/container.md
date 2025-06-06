# Container

**Framework**: CKTool JS  
**Kind**: struct

Details about a CloudKit container.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary Container {
	string id;
	string teamId;
	string name;
	string? imageUrl;
	boolean? isHidden;
};
```

#### Overview

Your app’s data is stored in a container. For information about what containers are available to you with CloudKit Console, see `https://icloud.developer.apple.com`. If you’re using Xcode, you can find your container identifier in your project’s Capability section.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { Container } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [id](container/id.md)
  The unique identifier of the container.
- [imageUrl](container/imageurl.md)
  The container’s image URL.
- [isHidden](container/ishidden.md)
  Whether the container is hidden.
- [name](container/name.md)
  The container name.
- [teamId](container/teamid.md)
  The identifier of the developer team who owns the container.

## See Also

- [ContainersResponse](containersresponse.md)
  An object that represents results of fetching multiple CloudKit containers.
- [CKEnvironment](ckenvironment.md)
  An enumeration of container environments.
- [ContainersSortByField](containerssortbyfield.md)
  An enumeration that indicates sorting options for retrieved containers.
- [SortDirection](sortdirection.md)
  An enumeration that indicates sorting direction when applying a custom sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/container)*