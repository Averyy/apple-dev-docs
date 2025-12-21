# withoutImplicitStartAccessing

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

This option causes an implicit call to [`startAccessingSecurityScopedResource()`](nsurl/startaccessingsecurityscopedresource().md) on the returned URL when it’s ready to use the resource.

This option isn’t applicable to security-scoped bookmarks.

## See Also

- [static var withoutUI: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutui.md)
  Specifies that no UI feedback should accompany resolution of the bookmark data.
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withSecurityScope: NSURL.BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions/withsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withoutimplicitstartaccessing)*