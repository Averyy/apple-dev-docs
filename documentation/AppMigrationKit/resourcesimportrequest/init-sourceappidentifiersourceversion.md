# init(sourceAppIdentifier:sourceVersion:)

**Framework**: AppMigrationKit  
**Kind**: init

Creates a resources import request instance for use in a unit test.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(sourceAppIdentifier: MigrationAppIdentifier, sourceVersion: String)
```

#### Discussion

You only use this initializer when creating unit tests that call [`importResources(from:importRequest:progress:)`](appmigrationtester/appimportcontroller/importresources(from:importrequest:progress:).md). Don’t use it in your app migration extension.

## Parameters

- `sourceAppIdentifier`: The application that exported the content.
- `sourceVersion`: The data format version provided by the source application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesimportrequest/init(sourceappidentifier:sourceversion:))*