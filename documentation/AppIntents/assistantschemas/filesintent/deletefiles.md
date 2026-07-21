# deleteFiles

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for deleting files.

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
var deleteFiles: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.files.deleteFiles` schema:

```swift
@AppIntent(schema: .files.deleteFiles)
struct DeleteFilesIntent: DeleteIntent {
    @Parameter
    var entities: [ExampleFileEntity]

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.files` app intent domain, see [`Files`](app-schema-domain-files.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/filesintent/deletefiles)*