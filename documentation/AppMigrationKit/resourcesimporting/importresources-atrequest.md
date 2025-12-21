# importResources(at:request:)

**Framework**: AppMigrationKit  
**Kind**: method  
**Required**: Yes

Imports resources to the app, in response to a request from the migration system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func importResources(at url: URL, request: ResourcesImportRequest) async throws
```

#### Discussion

Implement this method in your app extension to import files to your app from the source device. You can accomplish this task by moving all files from the directory indicated by `url` to an appropriate location for your app, such as the documents directory.

> ❗ **Important**: AppMigrationKit coerces any error thrown from this method into an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) instance. The framework persists this error so it can provide it to your app on its first launch. If your error can’t convert to an `NSError`, AppMigrationKit provides a generic error to the app instead.

## Parameters

- `url`: A URL that refers to a directory containing the resources to import.
- `request`: A request object that describes the source of the migration.

## See Also

- [struct ResourcesImportRequest](resourcesimportrequest.md)
  A type that exposes properties of the resources import request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting/importresources(at:request:))*