# NSURL.BookmarkCreationOptions

**Framework**: Foundation  
**Kind**: struct

Options used when creating bookmark data.

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
struct BookmarkCreationOptions
```

#### Overview

When creating a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md) method.

> **Note**:  Security-scoped bookmarks aren’t available in versions of macOS prior to 10.7.3.

 Security-scoped bookmarks aren’t available in versions of macOS prior to 10.7.3.

## Topics

### Creating a bookmark creation option
- [init(rawValue: UInt)](nsurl/bookmarkcreationoptions/init(rawvalue:).md)
  Initializes a new bookmark creation options structure.
### Options
- [static var minimalBookmark: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/minimalbookmark.md)
  Specifies that when creating a bookmark, it includes minimal information.
- [static var suitableForBookmarkFile: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [static var withSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withsecurityscope.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [static var securityScopeAllowOnlyReadAccess: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope.md)
  Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [static var preferFileIDResolution: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/preferfileidresolution.md)
  Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.
- [static var minimalBookmark: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/minimalbookmark.md)
  Specifies that when creating a bookmark, it includes minimal information.
- [static var suitableForBookmarkFile: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [static var withSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withsecurityscope.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [static var securityScopeAllowOnlyReadAccess: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope.md)
  Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [static var preferFileIDResolution: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/preferfileidresolution.md)
  Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.

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
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions)*