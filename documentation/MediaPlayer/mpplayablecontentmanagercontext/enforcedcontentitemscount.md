# enforcedContentItemsCount

**Framework**: Media Player  
**Kind**: property

Returns the number of content items to display during content limiting.

**Availability**:
- iOS 8.4+
- iPadOS 8.4+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var enforcedContentItemsCount: Int { get }
```

#### Discussion

This property returns [`NSIntegerMax`](https://developer.apple.com/documentation/ObjectiveC/NSIntegerMax) when the content server doesn’t limit the maximum number of items.

## See Also

- [var contentLimitsEnforced: Bool](mpplayablecontentmanagercontext/contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var endpointAvailable: Bool](mpplayablecontentmanagercontext/endpointavailable.md)
  Returns a Boolean that indicates whether the content server is available.
- [var enforcedContentTreeDepth: Int](mpplayablecontentmanagercontext/enforcedcontenttreedepth.md)
  The maximum depth of the navigation hierarchy allowed by the content server.
- [var contentLimitsEnabled: Bool](mpplayablecontentmanagercontext/contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/enforcedcontentitemscount)*