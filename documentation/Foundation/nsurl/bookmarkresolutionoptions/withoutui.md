# withoutUI

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that no UI feedback should accompany resolution of the bookmark data.

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
static var withoutUI: NSURL.BookmarkResolutionOptions { get }
```

```c
NSURLBookmarkResolutionWithoutUI
```

## See Also

### Constants
- [static var withoutMounting: NSURL.BookmarkResolutionOptions](./withoutmounting.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var withSecurityScope: NSURL.BookmarkResolutionOptions](./withsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [static var withoutImplicitStartAccessing: NSURL.BookmarkResolutionOptions](./withoutimplicitstartaccessing.md)
  A property that specifies that resolution doesn’t implicitly start accessing the ephemeral security-scoped resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkresolutionoptions/withoutui)*