# preferFileIDResolution

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that when creating a bookmark, upon resolution, its embedded file ID takes precedence over other sources of information (file system path, for example) when there’s a conflict.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 4.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This option does nothing and has no effect on bookmark resolution.

## Declaration

```swift
static var preferFileIDResolution: NSURL.BookmarkCreationOptions { get }
```

```c
NSURLBookmarkCreationPreferFileIDResolution
```

## See Also

### Options
- [static var minimalBookmark: NSURL.BookmarkCreationOptions](./minimalbookmark.md)
  Specifies that when creating a bookmark, it includes minimal information.
- [static var suitableForBookmarkFile: NSURL.BookmarkCreationOptions](./suitableforbookmarkfile.md)
  Specifies that the bookmark data includes the required properties for creating Finder alias files.
- [static var withSecurityScope: NSURL.BookmarkCreationOptions](./withsecurityscope.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read/write access to a file-system resource.
- [static var securityScopeAllowOnlyReadAccess: NSURL.BookmarkCreationOptions](./securityscopeallowonlyreadaccess.md)
  Specifies that when creating a security-scoped bookmark, upon resolution, it provides a security-scoped URL allowing read-only access to a file-system resource.
- [static var withoutImplicitSecurityScope: NSURL.BookmarkCreationOptions](./withoutimplicitsecurityscope.md)
  Prevents inclusion of a bookmark’s implicit ephemeral security scope, when creating one without security scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/preferfileidresolution)*