# standardizingPath

**Framework**: Foundation  
**Kind**: property

A new string made by removing extraneous path components from the receiver.

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
var standardizingPath: String { get }
```

#### Discussion

A new string made by performing the following operations:

- Expanding an initial tilde expression using [`expandingTildeInPath`](nsstring/expandingtildeinpath.md).
- Removing an initial component of “`/private/var/automount`”, “`/var/automount`”, or “`/private`” from the path, if the result still indicates an existing file or directory (checked by consulting the file system).
- Reducing empty components and references to the current directory (that is, the sequences  “//” and “/./”) to single path separators.
- Removing a trailing slash from the last component.
- For absolute paths only, resolving references to the parent directory (that is, the component “..”) to the real parent directory if possible using [`resolvingSymlinksInPath`](nsstring/resolvingsymlinksinpath.md). For relative paths, references to the parent directory are left in place.

Returns `self` if an error occurs.

Note that the path returned by this method may still have symbolic link components in it. Note also that this method only works with file paths (not, for example, string representations of URLs).

## See Also

- [class func path(withComponents: [String]) -> String](nsstring/path(withcomponents:).md)
  Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [var pathComponents: [String]](nsstring/pathcomponents.md)
  The file-system path components of the receiver.
- [func completePath(into: AutoreleasingUnsafeMutablePointer<NSString?>?, caseSensitive: Bool, matchesInto: AutoreleasingUnsafeMutablePointer<NSArray?>?, filterTypes: [String]?) -> Int](nsstring/completepath(into:casesensitive:matchesinto:filtertypes:).md)
  Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [var fileSystemRepresentation: UnsafePointer<CChar>](nsstring/filesystemrepresentation.md)
  A file system-specific representation of the receiver.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](nsstring/getfilesystemrepresentation(_:maxlength:).md)
  Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.
- [var isAbsolutePath: Bool](nsstring/isabsolutepath.md)
  A Boolean value that indicates whether the receiver represents an absolute path.
- [var lastPathComponent: String](nsstring/lastpathcomponent.md)
  The last path component of the receiver.
- [var pathExtension: String](nsstring/pathextension.md)
  The path extension, if any, of the string as interpreted as a path.
- [var abbreviatingWithTildeInPath: String](nsstring/abbreviatingwithtildeinpath.md)
  A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.
- [func appendingPathComponent(String) -> String](nsstring/appendingpathcomponent(_:).md)
  Returns a new string made by appending to the receiver a given string.
- [func appendingPathExtension(String) -> String?](nsstring/appendingpathextension(_:).md)
  Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [var deletingLastPathComponent: String](nsstring/deletinglastpathcomponent.md)
  A new string made by deleting the last path component from the receiver, along with any final path separator.
- [var deletingPathExtension: String](nsstring/deletingpathextension.md)
  A new string made by deleting the extension (if any, and only the last) from the receiver.
- [var expandingTildeInPath: String](nsstring/expandingtildeinpath.md)
  A new string made by expanding the initial component of the receiver to its full path value.
- [var resolvingSymlinksInPath: String](nsstring/resolvingsymlinksinpath.md)
  A new string made from the receiver by resolving all symbolic links and standardizing path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/standardizingpath)*