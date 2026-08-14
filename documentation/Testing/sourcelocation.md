# SourceLocation

**Framework**: Swift Testing  
**Kind**: struct

A type representing a location in source code.

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
struct SourceLocation
```

## Topics

### Initializers
- [init(fileID: String, filePath: String, line: Int, column: Int)](sourcelocation/init(fileid:filepath:line:column:).md)
  Initialize an instance of this type with the specified location details.
### Instance Properties
- [var column: Int](sourcelocation/column.md)
  The column in the source file.
- [var fileID: String](sourcelocation/fileid.md)
  The file ID of the source file.
- [var fileName: String](sourcelocation/filename.md)
  The name of the source file.
- [var filePath: String](sourcelocation/filepath.md)
  The path to the source file.
- [var line: Int](sourcelocation/line.md)
  The line in the source file.
- [var moduleName: String](sourcelocation/modulename.md)
  The name of the module containing the source file.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/sourcelocation)*