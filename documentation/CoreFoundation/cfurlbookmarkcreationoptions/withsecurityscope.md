# withSecurityScope

**Framework**: Core Foundation  
**Kind**: property

Specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read/write access to a file-system resource; for use in an app that adopts App Sandbox.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
static var withSecurityScope: CFURLBookmarkCreationOptions { get }
```

## See Also

- [static var preferFileIDResolutionMask: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/preferfileidresolutionmask.md)
  Specifies that an alias created with the bookmark data prefers resolving with its embedded file ID.
- [static var minimalBookmarkMask: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/minimalbookmarkmask.md)
  Specifies that an alias created with the bookmark data be created with minimal information, which may make it smaller but still able to resolve in certain ways.
- [static var suitableForBookmarkFile: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/suitableforbookmarkfile.md)
  Specifies that the bookmark data include properties required to create Finder alias files.
- [static var securityScopeAllowOnlyReadAccess: CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions/securityscopeallowonlyreadaccess.md)
  When combined with the [`withSecurityScope`](cfurlbookmarkcreationoptions/withsecurityscope.md) option, specifies that you want to create a security-scoped bookmark that, when resolved, provides a security-scoped URL allowing read-only access to a file-system resource; for use in an app that adopts App Sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/withsecurityscope)*