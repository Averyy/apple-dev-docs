# fileExists(atPath:isDirectory:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a file or directory exists at a specified path.

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
func fileExists(atPath path: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a file at the specified path exists, or [`false`](https://developer.apple.com/documentation/swift/false) if the file’s does not exist or its existence could not be determined.

#### Discussion

If the file at `path` is inaccessible to your app, perhaps because one or more parent directories are inaccessible, this method returns [`false`](https://developer.apple.com/documentation/swift/false). If the final element in `path` specifies a symbolic link, this method traverses the link and returns [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false) based on the existence of the file at the link destination.

If you need to further determine whether `path` is a package, use the [`isFilePackage(atPath:)`](https://developer.apple.com/documentation/AppKit/NSWorkspace/isFilePackage(atPath:)) method of [`NSWorkspace`](https://developer.apple.com/documentation/AppKit/NSWorkspace).

The following example code gets an array that identifies the fonts in the user’s fonts directory:

```objc
NSArray *subpaths;
BOOL isDir;
 
NSArray *paths = NSSearchPathForDirectoriesInDomains
                     (NSLibraryDirectory, NSUserDomainMask, YES);
 
if ([paths count] == 1) {
 
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSString *fontPath = [[paths objectAtIndex:0] stringByAppendingPathComponent:@"Fonts"];
 
    if ([fileManager fileExistsAtPath:fontPath isDirectory:&isDir] && isDir) {
        subpaths = [fileManager subpathsAtPath:fontPath];
// ...
```

> **Note**:  Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file-system race conditions, see [`Race Conditions and Secure File Operations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

 Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file-system race conditions, see [`Race Conditions and Secure File Operations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Parameters

- `path`: The path of a file or directory. If   begins with a tilde ( ), it must first be expanded with  , or this method will return  .
- `isDirectory`: Upon return, contains   if   is a directory or if the final path element is a symbolic link that points to a directory; otherwise, contains  . If   doesn’t exist, this value is undefined upon return. Pass   if you do not need this information.

## See Also

- [func checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkresourceisreachableandreturnerror(_:).md)
  Returns whether the resource pointed to by a file URL can be reached.
- [func fileExists(atPath: String) -> Bool](filemanager/fileexists(atpath:).md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func isReadableFile(atPath: String) -> Bool](filemanager/isreadablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [func isWritableFile(atPath: String) -> Bool](filemanager/iswritablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.
- [func isExecutableFile(atPath: String) -> Bool](filemanager/isexecutablefile(atpath:).md)
  Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [func isDeletableFile(atPath: String) -> Bool](filemanager/isdeletablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/fileexists(atpath:isdirectory:))*