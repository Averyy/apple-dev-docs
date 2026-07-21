# systemPrefersReducedResourceUsageDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when [`systemPrefersReducedResourceUsage`](uiapplication/systemprefersreducedresourceusage.md) changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
class let systemPrefersReducedResourceUsageDidChangeNotification: NSNotification.Name
```

#### Discussion

The object of the notification is the `UIApplication` object. The `userInfo` dictionary is empty. Re-read `systemPrefersReducedResourceUsage` to get the new value.

Use this notification to re-read the value and adjust the scheduling of future work, the same way the property is read proactively. Avoid performing or scheduling expensive work directly in the handler, as this could worsen resource usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/systemprefersreducedresourceusagedidchangenotification)*