# contentLimitsEnforced

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the content server enforces content limits.

**Availability**:
- iOS 8.4+ - Deprecated in 14.0
- iPadOS 8.4+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
var contentLimitsEnforced: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL contentLimitsEnforced;
```

## See Also

### Inspecting content manager properties
- [var endpointAvailable: Bool](./endpointavailable.md)
  Returns a Boolean that indicates whether the content server is available.
- [var enforcedContentItemsCount: Int](./enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var enforcedContentTreeDepth: Int](./enforcedcontenttreedepth.md)
  The maximum depth of the navigation hierarchy allowed by the content server.
- [var contentLimitsEnabled: Bool](./contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/contentlimitsenforced)*