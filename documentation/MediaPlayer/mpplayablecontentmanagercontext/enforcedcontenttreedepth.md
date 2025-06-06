# enforcedContentTreeDepth

**Framework**: Media Player  
**Kind**: property

The maximum depth of the navigation hierarchy allowed by the content server.

**Availability**:
- iOS 8.4+
- iPadOS 8.4+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var enforcedContentTreeDepth: Int { get }
```

#### Discussion

Exceeding the limit contained by this property causes your app to terminate.

## See Also

- [var contentLimitsEnforced: Bool](mpplayablecontentmanagercontext/contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var endpointAvailable: Bool](mpplayablecontentmanagercontext/endpointavailable.md)
  Returns a Boolean that indicates whether the content server is available.
- [var enforcedContentItemsCount: Int](mpplayablecontentmanagercontext/enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var contentLimitsEnabled: Bool](mpplayablecontentmanagercontext/contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/enforcedcontenttreedepth)*