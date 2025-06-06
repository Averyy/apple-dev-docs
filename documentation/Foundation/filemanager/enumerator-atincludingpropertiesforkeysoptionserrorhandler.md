# enumerator(at:includingPropertiesForKeys:options:errorHandler:)

**Framework**: Foundation  
**Kind**: method

Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@nonobjc
func enumerator(at url: URL, includingPropertiesForKeys keys: [URLResourceKey]?, options mask: FileManager.DirectoryEnumerationOptions = [], errorHandler handler: ((URL, any Error) -> Bool)? = nil) -> FileManager.DirectoryEnumerator?
```

#### Return Value

An directory enumerator object that enumerates the contents of the directory at `url`. If `url` is a filename, the method returns an enumerator object that enumerates no files—the first call to [`nextObject()`](nsenumerator/nextobject().md) returns nil.

#### Discussion

Because the enumeration is deep—that is, it lists the contents of all subdirectories—this enumerator object is useful for performing actions that involve large file-system subtrees. If the method is passed a directory on which another file system is mounted (a mount point), it traverses the mount point. This method does not resolve symbolic links or mount points encountered in the enumeration process, nor does it recurse through them if they point to a directory.

For example, if you pass a URL that points to `/Volumes/MyMountedFileSystem`, the returned enumerator will include the entire directory structure for the file system mounted at that location. If, on the other hand, you pass `/Volumes`, the returned enumerator will include `/Volumes/MyMountedFileSystem` as one of its results, but will not traverse into the file system mounted there.

The [`FileManager.DirectoryEnumerator`](filemanager/directoryenumerator.md) class has methods for skipping descendants of the existing path and for returning the number of levels deep the current object is in the directory hierarchy being enumerated (where the directory passed to [`enumerator(at:includingPropertiesForKeys:options:errorHandler:)`](filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:).md) is considered to be level 0).

This code fragment enumerates a URL and its subdirectories, collecting the URLs of files (skips directories). It also demonstrates how to ignore the contents of specified directories, in this case directories named “`_extras`”.

```swift
let directoryURL = Bundle.main.bundleURL
let localFileManager = FileManager()
 
let resourceKeys = Set<URLResourceKey>([.nameKey, .isDirectoryKey])
let directoryEnumerator = localFileManager.enumerator(at: directoryURL, includingPropertiesForKeys: Array(resourceKeys), options: .skipsHiddenFiles)!
 
var fileURLs: [URL] = []
for case let fileURL as URL in directoryEnumerator {
    guard let resourceValues = try? fileURL.resourceValues(forKeys: resourceKeys),
        let isDirectory = resourceValues.isDirectory,
        let name = resourceValues.name
        else {
            continue
    }
    
    if isDirectory {
        if name == "_extras" {
            directoryEnumerator.skipDescendants()
        }
    } else {
        fileURLs.append(fileURL)
    }
}
 
print(fileURLs)
```

## Parameters

- `url`: The location of the directory for which you want an enumeration. This URL must not be a symbolic link that points to the desired directory. You can use the   method to resolve any symlinks in the URL.
- `keys`: An array of keys that identify the properties that you want pre-fetched for each item in the enumeration. The values for these keys are cached in the corresponding   objects. You may specify nil for this parameter. For a list of keys you can specify, see  .
- `mask`: Options for the enumeration. For a list of valid options, see  .
- `handler`: If you specify   for this parameter, the enumerator object continues to enumerate items as if you had specified a block that returned  .

## See Also

- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
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
- [func subpaths(atPath: String) -> [String]?](filemanager/subpaths(atpath:).md)
  Returns an array of strings identifying the paths for all items in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:))*