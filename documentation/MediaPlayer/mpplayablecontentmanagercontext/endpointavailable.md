# endpointAvailable

**Framework**: Media Player  
**Kind**: property

Returns a Boolean that indicates whether the content server is available.

**Availability**:
- iOS 8.4+
- iPadOS 8.4+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var endpointAvailable: Bool { get }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the content server is available.

## See Also

- [var contentLimitsEnforced: Bool](mpplayablecontentmanagercontext/contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var enforcedContentItemsCount: Int](mpplayablecontentmanagercontext/enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var enforcedContentTreeDepth: Int](mpplayablecontentmanagercontext/enforcedcontenttreedepth.md)
  The maximum depth of the navigation hierarchy allowed by the content server.
- [var contentLimitsEnabled: Bool](mpplayablecontentmanagercontext/contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/endpointavailable)*