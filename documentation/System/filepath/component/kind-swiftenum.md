# FilePath.Component.Kind

**Framework**: System  
**Kind**: enum

Whether a component is a regular file or directory name, or a special directory `.` or `..`

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum Kind
```

## Topics

### Operators
- [static func == (FilePath.Component.Kind, FilePath.Component.Kind) -> Bool](filepath/component/kind-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FilePath.Component.Kind.currentDirectory](filepath/component/kind-swift.enum/currentdirectory.md)
  The special directory `.`, representing the current directory.
- [FilePath.Component.Kind.parentDirectory](filepath/component/kind-swift.enum/parentdirectory.md)
  The special directory `..`, representing the parent directory.
- [FilePath.Component.Kind.regular](filepath/component/kind-swift.enum/regular.md)
  A file or directory name
### Instance Properties
- [var hashValue: Int](filepath/component/kind-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](filepath/component/kind-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](filepath/component/kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/component/kind-swift.enum)*