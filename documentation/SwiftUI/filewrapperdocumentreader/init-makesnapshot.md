# init(_:makeSnapshot:)

**Framework**: SwiftUI  
**Kind**: init

Creates a reader that converts a `FileWrapper` into a snapshot.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ configuration: sending FileWrapperDocumentReader<Snapshot>.ReadConfiguration, makeSnapshot: @escaping (FileWrapper) async throws -> sending Snapshot)
```

## Parameters

- `configuration`: The read configuration passed to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- `makeSnapshot`: A closure that deserializes the `FileWrapper` into a snapshot. For flat files, read `regularFileContents`. For packages, navigate `fileWrappers` to find children. Throw an error if the data is malformed.

## See Also

- [FileWrapperDocumentReader.ReadConfiguration](filewrapperdocumentreader/readconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader/init(_:makesnapshot:))*