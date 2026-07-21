# systemPrefersReducedResourceUsage

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system prefers that the app reduce its resource usage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var systemPrefersReducedResourceUsage: Bool { get }
```

#### Discussion

When this value is `YES`, the system has entered a state where it would prefer apps to scale back resource-intensive work.

Use this to avoid or reduce expensive work. For example:

- Gate or simplify resource-intensive UI, such as 3D or AR viewers, advanced camera modes, or live effects.
- Choose lighter-weight paths, such as lower-resolution assets or fewer simultaneous operations.
- Defer or shrink non-essential background work, such as prefetching or precomputation.

Avoid performing or scheduling expensive work in response to changes in this property, as this could worsen resource usage.

> 💡 **Tip**: For in-memory caching, consider using `NSCache` with `NSPurgeableData`, which automatically evicts entries under system memory pressure. Use `systemPrefersReducedResourceUsage` for higher-level decisions that `NSCache` cannot make on its own.

To respond to changes in views, read the `UITraitCollection/systemPrefersReducedResourceUsage` trait. From other contexts, observe [`systemPrefersReducedResourceUsageDidChangeNotification`](uiapplication/systemprefersreducedresourceusagedidchangenotification.md) and re-read this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/systemprefersreducedresourceusage)*