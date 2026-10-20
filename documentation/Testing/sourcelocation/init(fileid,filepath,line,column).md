# init(fileID:filePath:line:column:)

**Framework**: Swift Testing  
**Kind**: init  
**Role**: Initializer

Initialize an instance of this type with the specified location details.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
init(fileID: String, filePath: String, line: Int, column: Int)
```

#### Discussion

> **Precondition**: `fileID` must not be empty and must be formatted as described in the documentation for [#fileID](../../Swift/fileid%28%29.md).

> **Precondition**: `line` must be greater than `0`.

> **Precondition**: `column` must be greater than `0`.

## Parameters

- `fileID`: The file ID of the source file, using the format described in the documentation for the [#fileID](../../Swift/fileid%28%29.md) macro in the Swift standard library.
- `filePath`: The path to the source file.
- `line`: The line in the source file. Must be greater than `0`.
- `column`: The column in the source file. Must be greater than `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/sourcelocation/init(fileid:filepath:line:column:))*