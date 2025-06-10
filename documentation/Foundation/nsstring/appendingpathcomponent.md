# appendingPathComponent(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made by appending to the receiver a given string.

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
func appendingPathComponent(_ str: String) -> String
```

#### Return Value

A new string made by appending `aString` to the receiver, preceded if necessary by a path separator.

#### Discussion

The following table illustrates the effect of this method on a variety of different paths, assuming that `aString` is supplied as “`scratch.tiff`”:

| Receiver’s String Value | Resulting String |
| --- | --- |
| “`/tmp`” | “`/tmp/scratch.tiff`” |
| “`/tmp/`” | “`/tmp/scratch.tiff`” |
| “`/`” | “`/scratch.tiff`” |
| “” (an empty string) | “`scratch.tiff`” |

Note that this method only works with file paths (not, for example, string representations of URLs).

## Parameters

- `str`: The path component to append to the receiver.

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
- [var standardizingPath: String](nsstring/standardizingpath.md)
  A new string made by removing extraneous path components from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/appendingpathcomponent(_:))*