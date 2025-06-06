# init(configuration:)

**Framework**: Swiftui  
**Kind**: init  
**Required**: Yes

Creates a document and initializes it with the contents of a file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(configuration: Self.ReadConfiguration) throws
```

#### Discussion

SwiftUI calls this initializer when someone opens a file type that matches one of those that your document type supports. Use the [`file`](filedocumentreadconfiguration/file.md) property of the `configuration` input to get document’s data. Deserialize the data, and store it in your document’s data structure:

```swift
init(configuration: ReadConfiguration) throws {
    guard let data = configuration.file.regularFileContents
    else { /* Throw an error. */ }
    model = try JSONDecoder().decode(Model.self, from: data)
}
```

The above example assumes that you define `Model` to contain the document’s data, that `Model` conforms to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol, and that you store a `model` property of that type inside your document.

> **Note**: SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## Parameters

- `configuration`: Information about the file that you read   document data from.

## See Also

- [static var readableContentTypes: [UTType]](referencefiledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReferenceFileDocument.ReadConfiguration](referencefiledocument/readconfiguration.md)
  The configuration for reading document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/init(configuration:))*