# withSecurityScope

**Framework**: Foundation  
**Kind**: property

Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var withSecurityScope: NSURL.BookmarkCreationOptions { get }
```

#### Discussion

For use in an app that adopts App Sandbox. For more information, see [`App Sandbox Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

> **Note**:  This flag can’t be used in conjunction with either [`minimalBookmark`](nsurl/bookmarkcreationoptions/minimalbookmark.md) or [`suitableForBookmarkFile`](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md).

## See Also

- [static var minimalBookmark: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/minimalbookmark.md)
  Specifies that when creating a bookmark, it includes minimal information.
- [static var suitableForBookmarkFile: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data includes the required properties for creating Finder alias files.
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
- [static var securityScopeAllowOnlyReadAccess: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/withoutimplicitsecurityscope.md)
  Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.
- [static var preferFileIDResolution: NSURL.BookmarkCreationOptions](nsurl/bookmarkcreationoptions/preferfileidresolution.md)
  Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/withsecurityscope)*