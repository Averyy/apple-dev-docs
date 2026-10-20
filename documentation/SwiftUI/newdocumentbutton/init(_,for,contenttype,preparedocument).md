# init(_:for:contentType:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+ - Deprecated in 27.2
- macOS 15.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Conform your document type to ReadableDocument instead.

## Declaration

```swift
@export(implementation)
nonisolated init<D>(_ title: LocalizedStringResource, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<D>(_ title: LocalizedStringResource, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
nonisolated
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ title: LocalizedStringKey, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
nonisolated
init<D>(_ title: LocalizedStringKey, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ title: some StringProtocol, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
nonisolated
init<D>(_ title: some StringProtocol, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

## Parameters

- `title`: A title resource for the button.
- `documentType`: A type of the document to create.
- `contentType`: An optional content type of the document to create.
- `prepareDocument`: A closure is called when a user presses the button. At this point, you can present a document template picker or another UI that allows users to choose a theme, configuration, or a template to create a document from. Return a prepared document, or throw an error if document creation failed. Return `nil` to request creation of an empty document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:))*