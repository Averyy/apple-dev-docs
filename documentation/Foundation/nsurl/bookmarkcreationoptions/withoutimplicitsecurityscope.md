# withoutImplicitSecurityScope

**Framework**: Foundation  
**Kind**: property

Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions { get }
```

#### Discussion

Bookmarks that you create without security scope automatically carry implicit ephemeral security scope. This security scope is valid until reboot at the latest, and confers access to the resource to any other process that resolves the bookmark. Using this option prevents inclusion of this ephemeral security scope.

When using this option, other processes can’t call [`startAccessingSecurityScopedResource()`](nsurl/startaccessingsecurityscopedresource().md) on the resolved URL. The option prevents providing unintended access to resources to other processes, and is also a performance optimization that reduces the size of the bookmark.

## See Also

- [static var minimalBookmark: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/minimalbookmark.md)
  Specifies that when creating a bookmark, it includes minimal information.
- [static var suitableForBookmarkFile: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [static var withSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withsecurityscope.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [static var securityScopeAllowOnlyReadAccess: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
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
- [static var preferFileIDResolution: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/preferfileidresolution.md)
  Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope)*