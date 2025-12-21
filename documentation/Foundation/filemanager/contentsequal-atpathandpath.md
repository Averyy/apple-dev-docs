# contentsEqual(atPath:andPath:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contentsEqual(atPath path1: String, andPath path2: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if file or directory specified in `path1` has the same contents as that specified in `path2`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If `path1` and `path2` are directories, the contents are the list of files and subdirectories each contains—contents of subdirectories are also compared. For files, this method checks to see if they’re the same file, then compares their size, and finally compares their contents. This method does not traverse symbolic links, but compares the links themselves.

## Parameters

- `path1`: The path of a file or directory to compare with the contents of  .
- `path2`: The path of a file or directory to compare with the contents of  .

## See Also

- [func contents(atPath: String) -> Data?](filemanager/contents(atpath:).md)
  Returns the contents of the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/contentsequal(atpath:andpath:))*