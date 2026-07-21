# systemPrefersReducedResourceUsage

**Framework**: SwiftUI  
**Kind**: property

A boolean value indicating whether the system would prefer the app to reduce its overall resource usage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var systemPrefersReducedResourceUsage: Bool { get set }
```

#### Discussion

When this value is `true`, the system has entered a state where it would prefer apps to scale back resource-intensive work. The default value is `false`.

Use this to avoid or reduce expensive work. For example:

- Gate or simplify resource-intensive UI, such as 3D or AR viewers, advanced camera modes, or live effects.
- Choose lighter-weight paths, such as lower-resolution assets or fewer simultaneous operations.
- Defer or shrink non-essential background work, such as prefetching or precomputation.

Avoid performing or scheduling expensive work in response to changes in this property, as this could worsen resource usage.

> 💡 **Tip**: For in-memory caching, consider using `NSCache` with `NSPurgeableData`, which automatically evicts entries under system memory pressure. Use `systemPrefersReducedResourceUsage` for higher-level decisions that `NSCache` cannot make on its own.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/systemprefersreducedresourceusage)*