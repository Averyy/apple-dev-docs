# init(_:makeSnapshot:)

**Framework**: SwiftUI  
**Kind**: init

Creates a reader that uses `FileWrapper` to read documents from disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ configuration: sending FileWrapperDocumentReader<Snapshot>.ReadConfiguration, makeSnapshot: @escaping (FileWrapper) async throws -> sending Snapshot)
```

## Parameters

- `configuration`: Properties required to read a document from disk.
- `makeSnapshot`: Deserializes a `FileWrapper` into a `Snapshot`. Throw an error if the data is malformed.

## See Also

- [FileWrapperDocumentReader.ReadConfiguration](filewrapperdocumentreader/readconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader/init(_:makesnapshot:))*