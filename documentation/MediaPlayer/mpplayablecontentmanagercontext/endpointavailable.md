# endpointAvailable

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean that indicates whether the content server is available.

**Availability**:
- iOS 8.4+ - Deprecated in 14.0
- iPadOS 8.4+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
var endpointAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL endpointAvailable;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the content server is available.

## See Also

### Inspecting content manager properties
- [var contentLimitsEnforced: Bool](./contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var enforcedContentItemsCount: Int](./enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var enforcedContentTreeDepth: Int](./enforcedcontenttreedepth.md)
  The maximum depth of the navigation hierarchy allowed by the content server.
- [var contentLimitsEnabled: Bool](./contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/endpointavailable)*