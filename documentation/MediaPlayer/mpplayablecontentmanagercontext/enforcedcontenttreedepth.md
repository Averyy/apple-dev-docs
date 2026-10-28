# enforcedContentTreeDepth

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The maximum depth of the navigation hierarchy allowed by the content server.

**Availability**:
- iOS 8.4+ - Deprecated in 14.0
- iPadOS 8.4+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
var enforcedContentTreeDepth: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger enforcedContentTreeDepth;
```

## Discussion

Exceeding the limit contained by this property causes your app to terminate.

## See Also

### Inspecting content manager properties
- [var contentLimitsEnforced: Bool](./contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var endpointAvailable: Bool](./endpointavailable.md)
  Returns a Boolean that indicates whether the content server is available.
- [var enforcedContentItemsCount: Int](./enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var contentLimitsEnabled: Bool](./contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/enforcedcontenttreedepth)*