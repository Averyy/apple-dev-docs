# init(fileID:filePath:line:column:)

**Framework**: Testing  
**Kind**: init

Initialize an instance of this type with the specified location details.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
init(fileID: String, filePath: String, line: Int, column: Int)
```

#### Discussion

> **Note**: `fileID` must not be empty and must be formatted as described in the documentation for [`#fileID`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/fileID()).

> **Note**: `line` must be greater than `0`.

> **Note**: `column` must be greater than `0`.

## Parameters

- `fileID`: The file ID of the source file, using the format described in   the documentation for the     macro in the Swift standard library.
- `filePath`: The path to the source file.
- `line`: The line in the source file. Must be greater than  .
- `column`: The column in the source file. Must be greater than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/sourcelocation/init(fileid:filepath:line:column:))*