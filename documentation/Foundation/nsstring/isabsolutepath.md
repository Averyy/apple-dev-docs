# isAbsolutePath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver represents an absolute path.

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
var isAbsolutePath: Bool { get }
```

```objc
@property (readonly, getter=isAbsolutePath) BOOL absolutePath;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver (if interpreted as a path) represents an absolute path, otherwise [`false`](../../Swift/false.md).

See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for more information on paths.

Note that this method only works with file paths (not, for example, string representations of URLs). The method does not check the filesystem for the existence of the path (use [`fileExists(atPath:)`](../filemanager/fileexists%28atpath%29.md) or similar methods in [`FileManager`](../filemanager.md) for that task).

## See Also

### Working with Paths
- [class func path(withComponents: [String]) -> String](./path%28withcomponents%29.md)
  Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [var pathComponents: [String]](./pathcomponents.md)
  The file-system path components of the receiver.
- [func completePath(into: AutoreleasingUnsafeMutablePointer<NSString?>?, caseSensitive: Bool, matchesInto: AutoreleasingUnsafeMutablePointer<NSArray?>?, filterTypes: [String]?) -> Int](./completepath%28into,casesensitive,matchesinto,filtertypes%29.md)
  Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [var fileSystemRepresentation: UnsafePointer<CChar>](./filesystemrepresentation.md)
  A file system-specific representation of the receiver.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](./getfilesystemrepresentation%28_,maxlength%29.md)
  Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.
- [var lastPathComponent: String](./lastpathcomponent.md)
  The last path component of the receiver.
- [var pathExtension: String](./pathextension.md)
  The path extension, if any, of the string as interpreted as a path.
- [var abbreviatingWithTildeInPath: String](./abbreviatingwithtildeinpath.md)
  A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.
- [func appendingPathComponent(String) -> String](./appendingpathcomponent%28_%29.md)
  Returns a new string made by appending to the receiver a given string.
- [func appendingPathExtension(String) -> String?](./appendingpathextension%28_%29.md)
  Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [var deletingLastPathComponent: String](./deletinglastpathcomponent.md)
  A new string made by deleting the last path component from the receiver, along with any final path separator.
- [var deletingPathExtension: String](./deletingpathextension.md)
  A new string made by deleting the extension (if any, and only the last) from the receiver.
- [var expandingTildeInPath: String](./expandingtildeinpath.md)
  A new string made by expanding the initial component of the receiver to its full path value.
- [var resolvingSymlinksInPath: String](./resolvingsymlinksinpath.md)
  A new string made from the receiver by resolving all symbolic links and standardizing path.
- [var standardizingPath: String](./standardizingpath.md)
  A new string made by removing extraneous path components from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/isabsolutepath)*