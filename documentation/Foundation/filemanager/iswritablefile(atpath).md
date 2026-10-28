# isWritableFile(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.

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
func isWritableFile(atPath path: String) -> Bool
```

```objc
- (BOOL) isWritableFileAtPath:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) if the current process has write privileges for the file at `path`; otherwise [`false`](../../Swift/false.md) if the process does not have write privileges or the existence of the file could not be determined.

## Discussion

If the file at `path` is inaccessible to your app, perhaps because it does not have search privileges for one or more parent directories, this method returns [`false`](../../Swift/false.md). This method traverses symbolic links in the path. This method also uses the real user ID and group ID, as opposed to the effective user and group IDs, to determine if the file is writable.

> **Note**:  Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file system race conditions, see [Race Conditions and Secure File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Parameters

- `path`: A file path.

## See Also

### Determining access to files
- [func fileExists(atPath: String) -> Bool](./fileexists%28atpath%29.md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](./fileexists%28atpath,isdirectory%29.md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func isReadableFile(atPath: String) -> Bool](./isreadablefile%28atpath%29.md)
  Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [func isExecutableFile(atPath: String) -> Bool](./isexecutablefile%28atpath%29.md)
  Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [func isDeletableFile(atPath: String) -> Bool](./isdeletablefile%28atpath%29.md)
  Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/iswritablefile(atpath:))*