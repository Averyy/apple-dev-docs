# mountedVolumeURLs(includingResourceValuesForKeys:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of URLs that identify the mounted volumes available on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func mountedVolumeURLs(includingResourceValuesForKeys propertyKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions = []) -> [URL]?
```

```objc
- (NSArray<NSURL *> *) mountedVolumeURLsIncludingResourceValuesForKeys:(NSArray<NSString *> *) propertyKeys options:(NSVolumeEnumerationOptions) options;
```

#### Return Value

An array of `NSURL` objects identifying the mounted volumes.

> ❗ **Important**:  This method returns `nil` on platforms other than macOS.

#### Discussion

This call may block if I/O is required to determine values for the requested `propertyKeys`.

## Parameters

- `propertyKeys`: An array of keys that identify the file properties that you want pre-fetched for each volume. For each returned URL, the values for these keys are cached in the corresponding [`NSURL`](../nsurl.md) objects. You may specify `nil` for this parameter. For a list of keys you can specify, see Common File System Resource Keys.
- `options`: Option flags for the enumeration. For a list of possible values, see [`FileManager.VolumeEnumerationOptions`](./volumeenumerationoptions.md).

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
- [FileManager.VolumeEnumerationOptions](./volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](./mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](./subpathsofdirectory%28atpath%29.md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](./subpaths%28atpath%29.md)
  Returns an array of strings identifying the paths for all items in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:))*