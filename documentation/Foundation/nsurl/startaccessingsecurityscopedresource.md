# startAccessingSecurityScopedResource()

**Framework**: Foundation  
**Kind**: method

In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startAccessingSecurityScopedResource() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the request to access the resource succeeded; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

When you obtain a security-scoped URL, such as by resolving a security-scoped bookmark, you can’t immediately use the resource it points to. To make the resource available to your app, by way of adding its location to your app’s sandbox, call this method on the security-scoped URL. You can also use Core Foundation equivalent, the [`CFURLStartAccessingSecurityScopedResource(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLStartAccessingSecurityScopedResource(_:)) function.

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), then you must relinquish access as soon as you finish using the resource. Call the [`stopAccessingSecurityScopedResource()`](nsurl/stopaccessingsecurityscopedresource().md) method to relinquish access. You must balance each call to [`startAccessingSecurityScopedResource()`](nsurl/startaccessingsecurityscopedresource().md) for a given security-scoped URL with a call to [`stopAccessingSecurityScopedResource()`](nsurl/stopaccessingsecurityscopedresource().md). When you make the last balanced call to [`stopAccessingSecurityScopedResource()`](nsurl/stopaccessingsecurityscopedresource().md), you immediately lose access to the resource in question.

> ⚠️ **Warning**:  If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

 If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

> **Note**:  Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

 Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

## See Also

- [class func bookmarkData(withContentsOf: URL) throws -> Data](nsurl/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func resourceValues(forKeys: [URLResourceKey], fromBookmarkData: Data) -> [URLResourceKey : Any]?](nsurl/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [class func writeBookmarkData(Data, to: URL, options: NSURL.BookmarkFileCreationOptions) throws](nsurl/writebookmarkdata(_:to:options:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func stopAccessingSecurityScopedResource()](nsurl/stopaccessingsecurityscopedresource.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [typealias BookmarkFileCreationOptions](nsurl/bookmarkfilecreationoptions.md)
  Options used when creating file bookmark data
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/startaccessingsecurityscopedresource())*