# init(contentsOf:named:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: init

Initialize an instance of this type with the contents of the given URL.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
init(contentsOf url: URL, named preferredName: String? = nil, sourceLocation: SourceLocation = #_sourceLocation) async throws
```

#### Discussion

> **Note**: Any error that occurs attempting to read from `url`.

Use this initializer to create an instance of [`Attachment`](attachment.md) that represents a local file or directory:

```swift
let url = try await FoodTruck.saveMenu(as: .pdf)
let attachment = try await Attachment(contentsOf: url)
Attachment.record(attachment)
```

When you call this initializer and pass it the URL of a file, it reads or maps the contents of that file into memory. When you call this initializer and pass it the URL of a directory, it creates a temporary ZIP file of the directory before reading or mapping it into memory. These operations may take some time, so this initializer suspends the calling task until they are complete.

> ❗ **Important**: This initializer supports creating attachments from file URLs only. If you pass it a URL other than a file URL, such as an HTTPS URL, the testing library throws an error.

## Parameters

- `url`: The URL containing the attachment’s data.
- `preferredName`: The preferred name of the attachment when writing it to   a test report or to disk. If  , the name of the attachment is   derived from the last path component of  .
- `sourceLocation`: The source location of the call to this initializer.   This value is used when recording issues associated with the   attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/init(contentsof:named:sourcelocation:))*