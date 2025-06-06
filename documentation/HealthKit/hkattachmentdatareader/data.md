# data

**Framework**: HealthKit  
**Kind**: property

The abstract’s data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var data: Data { get async throws }
```

#### Discussion

Use this property to asynchronously access the attachment’s data as a single data object.

```swift
let data: Data
do {
    data = try await dataReader.data
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while accessing the attachment's data. \(error.localizedDescription) ***")
}
```

## See Also

- [var bytes: HKAttachment.AsyncBytes](hkattachmentdatareader/bytes.md)
  An asynchronous sequence that provides the attachment’s data.
- [var progress: Progress](hkattachmentdatareader/progress.md)
  An object you can use to track the progress while reading an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentdatareader/data)*