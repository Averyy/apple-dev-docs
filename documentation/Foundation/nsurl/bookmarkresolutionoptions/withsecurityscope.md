# withSecurityScope

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var withSecurityScope: NSURL.BookmarkResolutionOptions { get }
```

```c
NSURLBookmarkResolutionWithSecurityScope
```

## See Also

### Constants
- [static var withoutUI: NSURL.BookmarkResolutionOptions](./withoutui.md)
  Specifies that no UI feedback should accompany resolution of the bookmark data.
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](./withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions](./withoutimplicitstartaccessing.md)
  A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withsecurityscope)*