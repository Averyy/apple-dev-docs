# subpaths(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns an array of strings identifying the paths for all items in the specified directory.

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
func subpaths(atPath path: String) -> [String]?
```

#### Return Value

An array of [`NSString`](nsstring.md) objects, each of which contains the path of an item in the directory specified by `path`. If `path` is a symbolic link, this method traverses the link. This method returns `nil` if it cannot retrieve the device of the linked-to file.

#### Discussion

This method recurses the specified directory and its subdirectories. The method skips the “`.`” and “`..`” directories at each level of the recursion.

This method reveals every element of the subtree at `path`, including the contents of file packages (such as apps, nib files, and RTFD files). This code fragment gets the contents of `/System/Library/Fonts` after verifying that the directory exists:

```objc
BOOL isDir = NO;
NSArray *subpaths;
NSString *fontPath = @"/System/Library/Fonts";
NSFileManager *fileManager = [[NSFileManager alloc] init];
if ([fileManager fileExistsAtPath:fontPath isDirectory:&isDir] && isDir)
    subpaths = [fileManager subpathsAtPath:fontPath];
```

##### Special Considerations

In macOS 10.5 and later, use [`subpathsOfDirectory(atPath:)`](filemanager/subpathsofdirectory(atpath:).md) instead.

## Parameters

- `path`: The path of the directory to list.

## See Also

- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(atpath:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [FileManager.DirectoryEnumerator](filemanager/directoryenumerator.md)
  An object that enumerates the contents of a directory.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](filemanager/volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](filemanager/subpathsofdirectory(atpath:).md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/subpaths(atpath:))*