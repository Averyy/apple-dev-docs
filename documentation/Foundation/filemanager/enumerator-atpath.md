# enumerator(atPath:)

**Framework**: Foundation  
**Kind**: method

Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.

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
func enumerator(atPath path: String) -> FileManager.DirectoryEnumerator?
```

#### Return Value

A [`FileManager.DirectoryEnumerator`](filemanager/directoryenumerator.md) object that enumerates the contents of the directory at `path`.

#### Discussion

If `path` is a filename, the method returns an enumerator object that enumerates no files—the first call to [`nextObject()`](nsenumerator/nextobject().md) will return `nil`.

Because the enumeration is deep—that is, it lists the contents of all subdirectories—this enumerator object is useful for performing actions that involve large file-system subtrees. This method does not resolve symbolic links encountered in the traversal process, nor does it recurse through them if they point to a directory.

This code fragment enumerates the subdirectories and files under a user’s `Documents` directory and processes all files with an extension of `.doc`:

```objc
NSString *docsDir = [NSHomeDirectory() stringByAppendingPathComponent:  @"Documents"];
NSFileManager *localFileManager=[[NSFileManager alloc] init];
NSDirectoryEnumerator *dirEnum =
    [localFileManager enumeratorAtPath:docsDir];
 
NSString *file;
while ((file = [dirEnum nextObject])) {
    if ([[file pathExtension] isEqualToString: @"doc"]) {
        // process the document
        [self scanDocument: [docsDir stringByAppendingPathComponent:file]];
    }
}
```

The [`FileManager.DirectoryEnumerator`](filemanager/directoryenumerator.md) class has methods for obtaining the attributes of the existing path and of the parent directory and for skipping descendants of the existing path.

## Parameters

- `path`: The path of the directory to enumerate.

## See Also

- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [var currentDirectoryPath: String](filemanager/currentdirectorypath.md)
  The path to the program’s current directory.
- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [FileManager.DirectoryEnumerator](filemanager/directoryenumerator.md)
  An object that enumerates the contents of a directory.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](filemanager/volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](filemanager/subpathsofdirectory(atpath:).md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](filemanager/subpaths(atpath:).md)
  Returns an array of strings identifying the paths for all items in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/enumerator(atpath:))*