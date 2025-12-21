# getFileSystemRepresentation(_:maxLength:)

**Framework**: Foundation  
**Kind**: method

Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.

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
func getFileSystemRepresentation(_ cname: UnsafeMutablePointer<CChar>, maxLength max: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `buffer` is successfully filled with a file-system representation, otherwise [`false`](https://developer.apple.com/documentation/Swift/false) (for example, if `maxLength` would be exceeded or if the receiver can’t be represented in the file system’s encoding).

#### Discussion

This method operates by replacing the abstract path and extension separator characters (’`/`’ and ‘`.`’ respectively) with their equivalents for the operating system. If the system-specific path or extension separator appears in the abstract representation, the characters it is converted to depend on the system (unless they’re identical to the abstract separators).

Note that this method only works with file paths (not, for example, string representations of URLs).

The following example illustrates the use of the `maxLength` argument. The first method invocation returns failure as the file representation of the string (`@"/mach_kernel"`) is 12 bytes long and the value passed as the `maxLength` argument (`12`) does not allow for the addition of a `NULL` termination byte.

```objc
char filenameBuffer[13];
BOOL success;
success = [@"/mach_kernel" getFileSystemRepresentation:filenameBuffer maxLength:12];
// success == NO
// Changing the length to include the NULL character does work
success = [@"/mach_kernel" getFileSystemRepresentation:filenameBuffer maxLength:13];
// success == YES
```

## Parameters

- `cname`: Upon return, contains a C-string that represent the receiver as a system-independent path, plus the   termination byte. The size of   must be large enough to contain   bytes.
- `max`: The maximum number of bytes in the string to return in   (including a terminating   character, which this method adds).

## See Also

- [class func path(withComponents: [String]) -> String](nsstring/path(withcomponents:).md)
  Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [var pathComponents: [String]](nsstring/pathcomponents.md)
  The file-system path components of the receiver.
- [func completePath(into: AutoreleasingUnsafeMutablePointer<NSString?>?, caseSensitive: Bool, matchesInto: AutoreleasingUnsafeMutablePointer<NSArray?>?, filterTypes: [String]?) -> Int](nsstring/completepath(into:casesensitive:matchesinto:filtertypes:).md)
  Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [var fileSystemRepresentation: UnsafePointer<CChar>](nsstring/filesystemrepresentation.md)
  A file system-specific representation of the receiver.
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
- [var standardizingPath: String](nsstring/standardizingpath.md)
  A new string made by removing extraneous path components from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getfilesystemrepresentation(_:maxlength:))*