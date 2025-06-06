# NSURL.BookmarkResolutionOptions

**Framework**: Foundation  
**Kind**: struct

Options used when resolving bookmark data.

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
struct BookmarkResolutionOptions
```

#### Overview

When resolving a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [`URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:`](nsurl/urlbyresolvingbookmarkdata:options:relativetourl:bookmarkdataisstale:error:.md) method.

##### Version Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X 10.7.3.

## Topics

### Initializers
- [init(rawValue: UInt)](nsurl/bookmarkresolutionoptions/init(rawvalue:).md)
  Initializes a new resolution options structure.
### Constants
- [static var withoutUI: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutui.md)
  Specifies that no UI feedback should accompany resolution of the bookmark data.
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withSecurityScope: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing.md)
  A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.
- [static var withoutUI: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutui.md)
  Specifies that no UI feedback should accompany resolution of the bookmark data.
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withSecurityScope: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing.md)
  A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func bookmarkData(withContentsOf: URL) throws -> Data](nsurl/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func resourceValues(forKeys: [URLResourceKey], fromBookmarkData: Data) -> [URLResourceKey : Any]?](nsurl/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions)*