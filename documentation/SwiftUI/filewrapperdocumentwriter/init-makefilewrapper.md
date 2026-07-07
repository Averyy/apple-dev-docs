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
init(_ configuration: sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: @escaping (Snapshot, FileWrapper?) async throws -> FileWrapper)
```

## Parameters

- `configuration`: Properties required to write a document to disk.
- `makeFileWrapper`: Serializes a `Snapshot` into a `FileWrapper`. The closure takes the following parameters: - `snapshot`: The snapshot to serialize into a `FileWrapper`.
- `previous`: The previous file wrapper that can be reused to optimize writing. If the latest operation for the document was writing, it is the file wrapper used for writing. If the latest operation was reading, SwiftUI passes the file wrapper read by a companion `FileWrapperDocumentReader`.

## See Also

- [FileWrapperDocumentWriter.WriteConfiguration](filewrapperdocumentwriter/writeconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter/init(_:makefilewrapper:))*