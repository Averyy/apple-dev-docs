# FilePath.Component.Kind

**Framework**: System  
**Kind**: enum  
**Role**: Enumeration

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

### Enumeration Cases
- [FilePath.Component.Kind.currentDirectory](./kind-swift.enum/currentdirectory.md)
  The special directory `.`, representing the current directory.
- [FilePath.Component.Kind.parentDirectory](./kind-swift.enum/parentdirectory.md)
  The special directory `..`, representing the parent directory.
- [FilePath.Component.Kind.regular](./kind-swift.enum/regular.md)
  A file or directory name

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/component/kind-swift.enum)*