# minimalBookmark

**Framework**: Foundation  
**Kind**: property

Specifies that when creating a bookmark, it includes minimal information.

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
static var minimalBookmark: NSURL.BookmarkCreationOptions { get }
```

#### Discussion

This produces a smaller bookmark that can be resolved in fewer ways.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/minimalbookmark)*