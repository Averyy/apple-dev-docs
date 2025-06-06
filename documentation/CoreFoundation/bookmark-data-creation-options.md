# Bookmark Data Creation Options

**Framework**: Core Foundation

Options used when creating bookmark data.

#### Overview

When creating a bookmark, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](cfurlcreatebookmarkdata(_:_:_:_:_:_:).md) method.

##### Version Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## Topics

### Constants
- [static var preferFileIDResolutionMask: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/preferfileidresolutionmask.md)
  Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID.
- [static var minimalBookmarkMask: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/minimalbookmarkmask.md)
  Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [static var suitableForBookmarkFile: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data include properties required to create Finder alias files.
- [static var withSecurityScope: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/withsecurityscope.md)
  Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.
- [static var securityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  When combined with the [`withSecurityScope`](cfurlbookmarkcreationoptions/withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.

## See Also

- [Bookmark Data Resolution Options](bookmark-data-resolution-options.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/bookmark-data-creation-options)*