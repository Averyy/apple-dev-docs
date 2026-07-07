# createFolder

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a folder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var createFolder: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.files.createFolder` schema:

```swift
@AppIntent(schema: .files.createFolder)
struct CreateFolderIntent: AppIntent {
    @Parameter
    var target: ExampleFileEntity

    @Parameter
    var fileName: String?

    func perform() async throws -> some ReturnsValue<ExampleFileEntity> {
        let url = URL(fileURLWithPath: "some/path")
        return .result(
            value: ExampleFileEntity(id: try .file(url: url))
        )
    }
}
```

For more information about the `.files` app intent domain, see doc:Making-file-management-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/filesintent/createfolder)*