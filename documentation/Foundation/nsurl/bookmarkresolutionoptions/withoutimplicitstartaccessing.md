# withoutImplicitStartAccessing

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 11.2+
- tvOS 14.2+
- visionOS 1.0+
- watchOS 7.2+

## Declaration

```swift
static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions { get }
```

```c
NSURLBookmarkResolutionWithoutImplicitStartAccessing
```

## Discussion

This option causes an implicit call to [`startAccessingSecurityScopedResource()`](../startaccessingsecurityscopedresource%28%29.md) on the returned URL when it’s ready to use the resource.

This option isn’t applicable to security-scoped bookmarks.

## See Also

### Constants
- [static var withoutUI: NSURL.BookmarkResolutionOptions](./withoutui.md)
  Specifies that no UI feedback should accompany resolution of the bookmark data.
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](./withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withSecurityScope: NSURL.BookmarkResolutionOptions](./withsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing)*