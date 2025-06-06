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
- [var line: Int](sourcelocation/line.md)
  The line in the source file.
- [var moduleName: String](sourcelocation/modulename.md)
  The name of the module containing the source file.
### Default Implementations
- [Comparable Implementations](sourcelocation/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](sourcelocation/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](sourcelocation/customstringconvertible-implementations.md)
- [Decodable Implementations](sourcelocation/decodable-implementations.md)
- [Encodable Implementations](sourcelocation/encodable-implementations.md)
- [Equatable Implementations](sourcelocation/equatable-implementations.md)
- [Hashable Implementations](sourcelocation/hashable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/sourcelocation)*