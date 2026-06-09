# thread

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var thread: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app entity that conforms to the `mail.thread` schema:

```swift

@AppEntity(schema: .mail.thread)
struct MailThreadEntity: AppEntity {
struct MailThreadEntityQuery: EntityQuery {
func entities(for identifiers: [MailThreadEntity.ID]) async throws -> [MailThreadEntity] { [] }
}
static let defaultQuery = MailThreadEntityQuery()
var displayRepresentation: DisplayRepresentation { "Unimplemented" }

let id = UUID()


}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailentity/thread)*