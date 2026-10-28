# subpathsOfDirectory(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func subpathsOfDirectory(atPath path: String) throws -> [String]
```

```objc
- (NSArray<NSString *> *) subpathsOfDirectoryAtPath:(NSString *) path error:(NSError **) error;
```

## Return Value

An array of strings, each containing the path of an item in the directory specified by `path`. When using Objective-C, returns `nil` if an error occurred.

## Discussion

This method recurses the specified directory and its subdirectories. The method skips the “`.`” and “`..`” directories at each level of the recursion.

Because this method recurses the directory’s contents, you might not want to use it in performance-critical code. Instead, consider using the [`enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:`](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md) or [`enumerator(atPath:)`](./enumerator%28atpath%29.md) method to enumerate the directory contents yourself. Doing so gives you more control over the retrieval of items and more opportunities to complete the enumeration or perform other tasks at the same time.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

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
- [func subpaths(atPath: String) -> [String]?](./subpaths%28atpath%29.md)
  Returns an array of strings identifying the paths for all items in the specified directory.
### Related Documentation
- [- enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/subpathsofdirectory(atpath:))*