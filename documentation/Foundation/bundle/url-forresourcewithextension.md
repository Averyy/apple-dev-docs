# url(forResource:withExtension:)

**Framework**: Foundation  
**Kind**: method

Returns the file URL for the resource identified by the specified name and file extension.

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
func url(forResource name: String?, withExtension ext: String?) -> URL?
```

#### Return Value

The file URL for the resource file or `nil` if the file could not be located.

#### Discussion

If `extension` is an empty string or `nil`, the returned pathname is the first one encountered where the file name exactly matches `name`. For details on how localized resources are found, read [`The Bundle Search Pattern`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW7) in [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

## Parameters

- `name`: If you specify  , the method returns the first resource file it finds with the specified extension.
- `ext`: If   is an empty string or  , the extension is assumed not to exist and the file URL is the first file encountered that exactly matches  .

## See Also

- [func url(forResource: String?, withExtension: String?, subdirectory: String?) -> URL?](bundle/url(forresource:withextension:subdirectory:).md)
  Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/url(forresource:withextension:))*