# changeCurrentDirectoryPath(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) changeCurrentDirectoryPath:(NSString *) path;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, otherwise [`false`](../../Swift/false.md).

#### Discussion

All relative pathnames refer implicitly to the current working directory.

> ⚠️ **Warning**:  This method changes the current working directory for the current process, not just the receiver.

## Parameters

- `path`: The path of the directory to which to change.

## See Also

### Related Documentation
- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](./fileexists%28atpath,isdirectory%29.md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func contentsOfDirectory(atPath: String) throws -> [String]](./contentsofdirectory%28atpath%29.md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
### Managing the current directory
- [var currentDirectoryPath: String](./currentdirectorypath.md)
  The path to the program’s current directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/changecurrentdirectorypath(_:))*