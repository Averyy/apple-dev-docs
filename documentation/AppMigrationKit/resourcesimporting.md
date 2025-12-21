# ResourcesImporting

**Framework**: AppMigrationKit  
**Kind**: protocol

A protocol for exporting transportable resources in a streaming archive format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol ResourcesImporting : AppMigrationExtension
```

#### Overview

Conform to this protocol in your app extension to import transportable resources: files on disk that can you can copy as-is from the source device without converting to an intermediate transport format.

> ❗ **Important**: In the event of an error, the migration system clears the data container of the containing app to prevent apps receiving only partially imported state. However, the system doesn’t clear app group containers. To handle this situation, have your app handle errors by clearing any app group containers prior to importing your content.

## Topics

### Importing resources
- [func importResources(at: URL, request: ResourcesImportRequest) async throws](resourcesimporting/importresources(at:request:).md)
  Imports resources to the app, in response to a request from the migration system.
- [struct ResourcesImportRequest](resourcesimportrequest.md)
  A type that exposes properties of the resources import request.
### Expressing progress
- [var resourcesImportProgress: Progress](resourcesimporting/resourcesimportprogress.md)
  A value to indicate the extension’s progress as it imports resources.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [AppMigrationExtension](appmigrationextension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting)*