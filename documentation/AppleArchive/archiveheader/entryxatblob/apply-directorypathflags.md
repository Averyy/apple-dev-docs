# apply(directory:path:flags:)

**Framework**: Apple Archive  
**Kind**: method

Applies extended attributes to a filesystem object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func apply(directory: FilePath, path: FilePath, flags: ArchiveFlags = []) throws
```

## Parameters

- `directory`: The base directory of the filesystem object.
- `path`: The path, relative to  , to target filesystem object.
- `flags`: Flags that control the behavior of the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob/apply(directory:path:flags:))*