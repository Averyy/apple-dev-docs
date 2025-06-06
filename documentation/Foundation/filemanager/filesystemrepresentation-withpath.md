# fileSystemRepresentation(withPath:)

**Framework**: Foundation  
**Kind**: method

Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.

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
func fileSystemRepresentation(withPath path: String) -> UnsafePointer<CChar>
```

#### Return Value

A C-string representation of `path` that properly encodes Unicode strings for use by the file system.

#### Discussion

Use this method if your code calls system routines that expect C-string path arguments. If you use the C string beyond the scope of the current autorelease pool, you must copy it.

This method raises an exception if `path` is `nil` or contains the empty string. This method also throws an exception if the conversion of the string fails.

## Parameters

- `path`: A string object containing a path to a file. This parameter must not be   or contain the empty string.

## See Also

- [func string(withFileSystemRepresentation: UnsafePointer<CChar>, length: Int) -> String](filemanager/string(withfilesystemrepresentation:length:).md)
  Returns an [`NSString`](nsstring.md) object whose contents are derived from the specified C-string path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/filesystemrepresentation(withpath:))*