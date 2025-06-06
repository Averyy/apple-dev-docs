# currentDirectoryPath

**Framework**: Foundation  
**Kind**: property

The path to the program’s current directory.

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
var currentDirectoryPath: String { get }
```

#### Discussion

The current directory path is the starting point for any relative paths you specify. For example, if the current directory is `/tmp` and you specify a relative pathname of `reports/info.txt`, the resulting full path for the item is `/tmp/reports/info.txt`.

When an app is launched, this property is initially set to the app’s current working directory. If the current working directory is not accessible for any reason, the value of this property is `nil`. You can change the value of this property by calling the [`changeCurrentDirectoryPath(_:)`](filemanager/changecurrentdirectorypath(_:).md) method.

> ⚠️ **Warning**:  This property reports the current working directory for the current process, not just the receiver.

 This property reports the current working directory for the current process, not just the receiver.

## See Also

- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(atpath:withintermediatedirectories:attributes:).md)
  Creates a directory with given attributes at the specified path.
- [func changeCurrentDirectoryPath(String) -> Bool](filemanager/changecurrentdirectorypath(_:).md)
  Changes the path of the current working directory to the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/currentdirectorypath)*