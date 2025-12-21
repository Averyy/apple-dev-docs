# importResources(from:importRequest:progress:)

**Framework**: AppMigrationKit  
**Kind**: method

Tells the migration extension to begin importing transportable resources into the app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final func importResources(from extractedResourceURL: URL, importRequest: ResourcesImportRequest? = nil, progress: Progress? = nil) async throws
```

#### Discussion

Clean your app state before starting an import test, since the app extension runs on a clean app state. In particular, remove any files you previously wrote to the app container and ensure it’s empty. This simulates how the extension normally runs during a migration.

## Parameters

- `extractedResourceURL`: A file URL pointing to a directory that contains the resources to import.
- `importRequest`: An optional migration request instance to pass to the app extension’s import method. If this value is  , the framework uses a default request. This value defaults to  .
- `progress`: An optional   object the extension uses to report its progress back to the unit test. This value defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appimportcontroller/importresources(from:importrequest:progress:))*