# init(_:makeFileWrapper:)

**Framework**: SwiftUI  
**Kind**: init

Creates a writer that uses `FileWrapper` to write documents to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ configuration: sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: @escaping (Snapshot) async throws -> FileWrapper)
```

## Parameters

- `configuration`: Properties required to write a document to disk.
- `makeFileWrapper`: Serializes a `Snapshot` into a `FileWrapper`.

## See Also

- [FileWrapperDocumentWriter.WriteConfiguration](filewrapperdocumentwriter/writeconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter/init(_:makefilewrapper:))*