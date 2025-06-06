# url(forResource:withExtension:subdirectory:)

**Framework**: Foundation  
**Kind**: method

Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.

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
func url(forResource name: String?, withExtension ext: String?, subdirectory subpath: String?) -> URL?
```

#### Return Value

The file URL for the resource file or `nil` if the file could not be located. This method also returns `nil` if the bundle specified by the `bundlePath` parameter does not exist or is not a readable directory.

#### Discussion

For details on how localized resources are found, read [`The Bundle Search Pattern`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

## Parameters

- `name`: If you specify  , the method returns the first resource file it finds with the specified extension in that directory.
- `ext`: If you specify an empty string or  , the extension is assumed not to exist and the file URL is the first file encountered that exactly matches  .
- `subpath`: The path of a top-level bundle directory. This must be a valid path. For example, to specify the bundle directory for a Mac app, you might specify the path  .

## See Also

- [func url(forResource: String?, withExtension: String?) -> URL?](bundle/url(forresource:withextension:).md)
  Returns the file URL for the resource identified by the specified name and file extension.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?) -> [URL]?](bundle/urls(forresourceswithextension:subdirectory:).md)
  Returns an array of file URLs for all resources identified by the specified file extension and located in the specified bundle subdirectory.
- [func url(forResource: String?, withExtension: String?, subdirectory: String?, localization: String?) -> URL?](bundle/url(forresource:withextension:subdirectory:localization:).md)
  Returns the file URL for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?, localization: String?) -> [URL]?](bundle/urls(forresourceswithextension:subdirectory:localization:).md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func url(forResource: String?, withExtension: String?, subdirectory: String?, in: URL) -> URL?](bundle/url(forresource:withextension:subdirectory:in:).md)
  Creates and returns a file URL for the resource with the specified name and extension in the specified bundle.
- [class func urls(forResourcesWithExtension: String?, subdirectory: String?, in: URL) -> [URL]?](bundle/urls(forresourceswithextension:subdirectory:in:).md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, within the specified bundle.
- [func path(forResource: String?, ofType: String?) -> String?](bundle/path(forresource:oftype:).md)
  Returns the full pathname for the resource identified by the specified name and file extension.
- [func path(forResource: String?, ofType: String?, inDirectory: String?) -> String?](bundle/path(forresource:oftype:indirectory:)-swift.method.md)
  Returns the full pathname for the resource identified by the specified name and file extension and located in the specified bundle subdirectory.
- [func path(forResource: String?, ofType: String?, inDirectory: String?, forLocalization: String?) -> String?](bundle/path(forresource:oftype:indirectory:forlocalization:).md)
  Returns the full pathname for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [func paths(forResourcesOfType: String?, inDirectory: String?) -> [String]](bundle/paths(forresourcesoftype:indirectory:)-swift.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified filename extension and residing in the resource subdirectory.
- [func paths(forResourcesOfType: String?, inDirectory: String?, forLocalization: String?) -> [String]](bundle/paths(forresourcesoftype:indirectory:forlocalization:).md)
  Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func path(forResource: String?, ofType: String?, inDirectory: String) -> String?](bundle/path(forresource:oftype:indirectory:)-swift.type.method.md)
  Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [class func paths(forResourcesOfType: String?, inDirectory: String) -> [String]](bundle/paths(forresourcesoftype:indirectory:)-swift.type.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/url(forresource:withextension:subdirectory:))*