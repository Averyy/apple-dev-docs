# changeCurrentDirectoryPath(_:)

**Framework**: Foundation  
**Kind**: method

Changes the path of the current working directory to the specified path.

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
func changeCurrentDirectoryPath(_ path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

All relative pathnames refer implicitly to the current working directory.

> ⚠️ **Warning**:  This method changes the current working directory for the current process, not just the receiver.

 This method changes the current working directory for the current process, not just the receiver.

## Parameters

- `path`: The path of the directory to which to change.

## See Also

- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](filemanager/fileexists(atpath:isdirectory:).md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [var currentDirectoryPath: String](filemanager/currentdirectorypath.md)
  The path to the program’s current directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/changecurrentdirectorypath(_:))*