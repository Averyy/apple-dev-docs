# subpaths(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NSString *> *) subpathsAtPath:(NSString *) path;
```

#### Return Value

An array of [`NSString`](../nsstring.md) objects, each of which contains the path of an item in the directory specified by `path`. If `path` is a symbolic link, this method traverses the link. This method returns `nil` if it cannot retrieve the device of the linked-to file.

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

In macOS 10.5 and later, use [`subpathsOfDirectory(atPath:)`](./subpathsofdirectory%28atpath%29.md) instead.

## Parameters

- `path`: The path of the directory to list.

## See Also

### Discovering directory contents
- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](./contentsofdirectory%28at,includingpropertiesforkeys,options%29.md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](./contentsofdirectory%28atpath%29.md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](./enumerator%28at,includingpropertiesforkeys,options,errorhandler%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](./enumerator%28atpath%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [FileManager.DirectoryEnumerator](./directoryenumerator.md)
  An object that enumerates the contents of a directory.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](./mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](./volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](./mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](./subpathsofdirectory%28atpath%29.md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [- enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/subpaths(atpath:))*