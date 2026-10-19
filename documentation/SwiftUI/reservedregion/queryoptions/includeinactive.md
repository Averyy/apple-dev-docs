# includeInactive

**Framework**: SwiftUI  
**Kind**: property

An option that includes inactive reserved regions in the results.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
static var includeInactive: ReservedRegion.QueryOptions { get }
```

#### Discussion

By default, a query returns only the regions that are active. Include inactive regions to leave room for a region that isn’t active yet, so your layout doesn’t jump when the region becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/queryoptions/includeinactive)*