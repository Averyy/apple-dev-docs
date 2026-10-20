# ResourcesImportRequest

**Framework**: AppMigrationKit  
**Kind**: struct  
**Role**: Structure

A type that exposes properties of the resources import request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct ResourcesImportRequest
```

## Topics

### Creating an import request for testing
- [init(sourceAppIdentifier: MigrationAppIdentifier, sourceVersion: String)](./resourcesimportrequest/init%28sourceappidentifier,sourceversion%29.md)
  Creates a resources import request instance for use in a unit test.
### Inspecting import request properties
- [let sourceAppIdentifier: MigrationAppIdentifier](./resourcesimportrequest/sourceappidentifier.md)
  The application that exported the content.
- [struct MigrationAppIdentifier](./migrationappidentifier.md)
  A type that identifies an app on a different platform.
- [let sourceVersion: String](./resourcesimportrequest/sourceversion.md)
  The data format version provided by the source application.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Importing resources
- [func importResources(at: URL, request: ResourcesImportRequest) async throws](./resourcesimporting/importresources%28at,request%29.md)
  Imports resources to the app, in response to a request from the migration system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesimportrequest)*