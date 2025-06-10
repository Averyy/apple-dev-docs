# appendingPathExtension(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made by appending to the receiver an extension separator followed by a given extension.

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
func appendingPathExtension(_ str: String) -> String?
```

#### Return Value

A new string made by appending to the receiver an extension separator followed by `ext`.

#### Discussion

The following table illustrates the effect of this method on a variety of different paths, assuming that `ext` is supplied as `@"tiff"`:

| Receiver’s String Value | Resulting String |
| --- | --- |
| “`/tmp/scratch.old`” | “`/tmp/scratch.old.tiff`” |
| “`/tmp/scratch.`” | “`/tmp/scratch..tiff`” |
| “`/tmp/`” | “`/tmp.tiff`” |
| “`scratch`” | “`scratch.tiff`” |

Note that adding an extension to `@"/tmp/"` causes the result to be `@"/tmp.tiff"` instead of `@"/tmp/.tiff"`. This difference is because a file named `@".tiff"` is not considered to have an extension, so the string is appended to the last nonempty path component.

Note that this method only works with file paths (not, for example, string representations of URLs).

##### Special Considerations

Prior to OS X v10.9 this method did not allow you to append file extensions to filenames starting with the tilde character (`~`).

## Parameters

- `str`: The extension to append to the receiver.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/appendingpathextension(_:))*