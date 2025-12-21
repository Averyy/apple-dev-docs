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

## Parameters

- `url`: The URL containing the attachment’s data.
- `preferredName`: The preferred name of the attachment when writing it to   a test report or to disk. If  , the name of the attachment is   derived from the last path component of  .
- `sourceLocation`: The source location of the call to this initializer.   This value is used when recording issues associated with the   attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/init(contentsof:named:sourcelocation:))*