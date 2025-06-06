# string(withFileSystemRepresentation:length:)

**Framework**: Foundation  
**Kind**: method

Returns an [`NSString`](nsstring.md) object whose contents are derived from the specified C-string path.

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
func string(withFileSystemRepresentation str: UnsafePointer<CChar>, length len: Int) -> String
```

#### Return Value

An [`NSString`](nsstring.md) object converted from the C-string representation `string` with length `len` of a pathname in the current file system.

#### Discussion

Use this method if your code receives paths as C strings from system routines.

## Parameters

- `str`: A C string representation of a pathname.
- `len`: The number of characters in  .

## See Also

- [func fileSystemRepresentation(withPath: String) -> UnsafePointer<CChar>](filemanager/filesystemrepresentation(withpath:).md)
  Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/string(withfilesystemrepresentation:length:))*