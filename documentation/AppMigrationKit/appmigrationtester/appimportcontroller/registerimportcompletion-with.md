# registerImportCompletion(with:)

**Framework**: AppMigrationKit  
**Kind**: method

Tells your app that import completed with a given status.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final func registerImportCompletion(with status: MigrationStatus) async throws
```

#### Discussion

Use this method in a unit test to evaluate how your app handles a post-migration launch. You can uses success or failure statuses to see the different messages presented to the person using the app.

## Parameters

- `status`: A status value that indicates success or failure of the import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appimportcontroller/registerimportcompletion(with:))*