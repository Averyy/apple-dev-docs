# bytes

**Framework**: HealthKit  
**Kind**: property

An asynchronous sequence that provides the attachment’s data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var bytes: HKAttachment.AsyncBytes { get }
```

#### Discussion

Use this property to access the file’s contents as an asynchronous sequence of bytes.

```swift
// Asynchronously access the attachment's bytes.
var data = Data()
do {
    for try await byte in dataReader.bytes {
        // Use the bytes here.
        data.append(byte)
    }
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while reading the attachment's data: \(error.localizedDescription) ***")
}
```

## See Also

- [var data: Data](hkattachmentdatareader/data.md)
  The abstract’s data.
- [var progress: Progress](hkattachmentdatareader/progress.md)
  An object you can use to track the progress while reading an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentdatareader/bytes)*