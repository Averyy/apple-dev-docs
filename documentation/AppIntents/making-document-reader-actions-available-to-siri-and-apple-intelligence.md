# Making document reader actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s document viewing and editing functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s document viewing and editing capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent, app entity, and app enumeration implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows people to view and rotate a document, use the [`AppIntent(schema:)`](appintent(schema:).md) macro and provide the assistant schema that consists of the `.reader` domain and the [`rotatePages`](assistantschemas/readerintent/rotatepages.md) schema:

```swift
@AppIntent(schema: .reader.rotatePages)
struct ReaderRotatePagesIntent {
    var pages: [ReaderPageEntity]
    var isClockwise: Bool

    func perform() async throws -> some IntentResult & ReturnsValue<[ReaderPageEntity]> {
        return .result(value: [ReaderPageEntity]())
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.reader` domain, see [`AssistantSchemas.ReaderIntent`](assistantschemas/readerintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AppEntity(schema:)`](appentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `ReaderPageEntity`. The following code snippet shows how the `ReaderPageEntity` implementation uses the [`AppEntity(schema:)`](appentity(schema:).md) macro:

```swift
@AppEntity(schema: .reader.document)
struct ReaderDocumentEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [ReaderDocumentEntity.ID]) async throws -> [ReaderDocumentEntity] { [] }
        func entities(matching string: String) async throws -> [ReaderDocumentEntity] { [] }
    }
    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "A display representation." }

    let id = UUID()

    var title: String
    var kind: ReaderDocumentKind
    var width: Int?
    var height: Int?
}
```

The assistant schema for the `ReaderPageEntity` consists of the `.reader` domain and the [`document`](assistantschemas/readerentity/document.md) schema.

For a list of available app entity schemas in the `.reader` domain, see [`AssistantSchemas.ReaderEntity`](assistantschemas/readerentity.md).

##### Make Sure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AppEnum(schema:)`](appenum(schema:).md) macro. Then, pass the `.reader` domain and a schema to it. The following example uses the [`documentKind`](assistantschemas/readerenum/documentkind.md) schema:

```swift
import Foundation
import AppIntents

@AppEnum(schema: .reader.documentKind)
enum ReaderDocumentKind: String, AppEnum, Codable {
    case image
    case pdf

    static var caseDisplayRepresentations: [ReaderDocumentKind: DisplayRepresentation] = [:]
}

```

For a list of available app enumeration schemas in the `.reader` domain, see [`AssistantSchemas.ReaderEnum`](assistantschemas/readerenum.md).

## See Also

- [AssistantSchemas.ReaderIntent](assistantschemas/readerintent.md)
  Assistant schema conformance for app intents that offer document viewing and editing functionality.
- [AssistantSchemas.ReaderEntity](assistantschemas/readerentity.md)
  Assistant schema conformance for app entities that describe documents.
- [AssistantSchemas.ReaderEnum](assistantschemas/readerenum.md)
  Assistant schema conformance for types you use to describe documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-document-reader-actions-available-to-siri-and-apple-intelligence)*