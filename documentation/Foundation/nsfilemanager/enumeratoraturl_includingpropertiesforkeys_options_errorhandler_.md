# enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (NSDirectoryEnumerator<NSURL *> *) enumeratorAtURL:(NSURL *) url includingPropertiesForKeys:(NSArray<NSString *> *) keys options:(NSDirectoryEnumerationOptions) mask errorHandler:(BOOL (^)(NSURL *url, NSError *error)) handler;
```

## Return Value

An directory enumerator object that enumerates the contents of the directory at `url`. If `url` is a filename, the method returns an enumerator object that enumerates no files—the first call to [`nextObject()`](../nsenumerator/nextobject%28%29.md) returns `nil`.

## Discussion

Because the enumeration is deep—that is, it lists the contents of all subdirectories—this enumerator object is useful for performing actions that involve large file-system subtrees. If the method is passed a directory on which another file system is mounted (a mount point), it traverses the mount point. This method does not resolve symbolic links or mount points encountered in the enumeration process, nor does it recurse through them if they point to a directory.

For example, if you pass a URL that points to `/Volumes/MyMountedFileSystem`, the returned enumerator will include the entire directory structure for the file system mounted at that location. If, on the other hand, you pass `/Volumes`, the returned enumerator will include `/Volumes/MyMountedFileSystem` as one of its results, but will not traverse into the file system mounted there.

The [`FileManager.DirectoryEnumerator`](../filemanager/directoryenumerator.md) class has methods for skipping descendants of the existing path and for returning the number of levels deep the current object is in the directory hierarchy being enumerated (where the directory passed to [`enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:`](./enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md) is considered to be level 0).

This code fragment enumerates a URL and its subdirectories, collecting the URLs of files (skips directories). It also demonstrates how to ignore the contents of specified directories, in this case directories named “`_extras`”.

```objc
NSURL *directoryURL = [[NSBundle mainBundle] bundleURL];
NSFileManager *localFileManager= [[NSFileManager alloc] init];
NSDirectoryEnumerator *directoryEnumerator =
   [localFileManager enumeratorAtURL:directoryURL
          includingPropertiesForKeys:@[NSURLNameKey, NSURLIsDirectoryKey]
                             options:NSDirectoryEnumerationSkipsHiddenFiles
                        errorHandler:nil];
 
NSMutableArray<NSURL *> *mutableFileURLs = [NSMutableArray array];
for (NSURL *fileURL in directoryEnumerator) {
    NSNumber *isDirectory = nil;
    [fileURL getResourceValue:&isDirectory forKey:NSURLIsDirectoryKey error:nil];
 
    if ([isDirectory boolValue]) {
        NSString *name = nil;
        [fileURL getResourceValue:&name forKey:NSURLNameKey error:nil];
 
        if ([name isEqualToString:@"_extras"]) {
            [directoryEnumerator skipDescendants];
        } else {
            [mutableFileURLs addObject:fileURL];
        }
    }
}
 
NSLog(@"Files: %@", mutableFileURLs);
```

## Parameters

- `url`: The location of the directory for which you want an enumeration. This URL must not be a symbolic link that points to the desired directory. You can use the [`resolvingSymlinksInPath`](../nsurl/resolvingsymlinksinpath.md) method to resolve any symlinks in the URL.
- `keys`: An array of keys that identify the properties that you want pre-fetched for each item in the enumeration. The values for these keys are cached in the corresponding [`NSURL`](../nsurl.md) objects. You may specify `nil` for this parameter. For a list of keys you can specify, see [`URLResourceKey`](../urlresourcekey.md).
- `mask`: Options for the enumeration. For a list of valid options, see [`FileManager.DirectoryEnumerationOptions`](../filemanager/directoryenumerationoptions.md).
- `handler`: An optional error handler block for the file manager to call when an error occurs. The handler block should return [`true`](../../Swift/true.md) if you want the enumeration to continue or [`false`](../../Swift/false.md) if you want the enumeration to stop. The block takes the following parameters:

  - **url**: An [`NSURL`](../nsurl.md) object that identifies the item for which the error occurred.
  - **error**: An [`NSError`](../nserror.md) object that contains information about the error.

  If you specify `nil` for this parameter, the enumerator object continues to enumerate items as if you had specified a block that returned [`true`](../../Swift/true.md).

## See Also

### Discovering directory contents
- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](../filemanager/contentsofdirectory%28at,includingpropertiesforkeys,options%29.md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](../filemanager/contentsofdirectory%28atpath%29.md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](../filemanager/enumerator%28atpath%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [FileManager.DirectoryEnumerator](../filemanager/directoryenumerator.md)
  An object that enumerates the contents of a directory.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](../filemanager/mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](../filemanager/volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](../filemanager/mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](../filemanager/subpathsofdirectory%28atpath%29.md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](../filemanager/subpaths%28atpath%29.md)
  Returns an array of strings identifying the paths for all items in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanager/enumeratoraturl:includingpropertiesforkeys:options:errorhandler:)*