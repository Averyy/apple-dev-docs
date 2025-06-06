# resourceValues(forKeys:fromBookmarkData:)

**Framework**: Foundation  
**Kind**: method

Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.

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
class func resourceValues(forKeys keys: [URLResourceKey], fromBookmarkData bookmarkData: Data) -> [URLResourceKey : Any]?
```

#### Return Value

A dictionary of the requested resource values contained in `bookmarkData`.

## Parameters

- `keys`: An array of names of URL resource properties. In addition to the standard, system-defined resource properties, you can also request any custom properties that you provided when you created the bookmark. See the   method for details.
- `bookmarkData`: The bookmark data from which you want to retrieve resource values.

## See Also

- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
- [class func bookmarkData(withContentsOf: URL) throws -> Data](nsurl/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func writeBookmarkData(Data, to: URL, options: NSURL.BookmarkFileCreationOptions) throws](nsurl/writebookmarkdata(_:to:options:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func startAccessingSecurityScopedResource() -> Bool](nsurl/startaccessingsecurityscopedresource.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func stopAccessingSecurityScopedResource()](nsurl/stopaccessingsecurityscopedresource.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [typealias BookmarkFileCreationOptions](nsurl/bookmarkfilecreationoptions.md)
  Options used when creating file bookmark data
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/resourcevalues(forkeys:frombookmarkdata:))*