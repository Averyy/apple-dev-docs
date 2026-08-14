# CTSlicingManager.AppCategory

**Framework**: Core Telephony  
**Kind**: enum

App categories for network slicing.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
enum AppCategory
```

#### Discussion

Network slicing allows carriers to optimize their network for specific types of apps. The `AppCategory` enumeration defines the supported app types that can use network slicing.

A category is available for use only when you meet all of the following conditions:

- The carrier’s network supports the specific slice category (for example, a carrier may support communication slices, but not gaming slices).
- Your app has the appropriate entitlements for that category. To enable network slicing, you need to set the [`5G Network Slicing Traffic Category`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.slicing.trafficcategory) entitlement.
- The device and network conditions allow network slicing.

Always check [`availableSliceAppCategories`](ctslicingmanager/availablesliceappcategories.md) before attempting to activate a category because availability depends on both carrier network support and your app’s entitlements.

## Topics

### App categories
- [CTSlicingManager.AppCategory.gaming](ctslicingmanager/appcategory/gaming.md)
  An application category for gaming traffic requiring low latency.
- [CTSlicingManager.AppCategory.communication](ctslicingmanager/appcategory/communication.md)
  An application category for voice, video calling, and messaging services.
- [CTSlicingManager.AppCategory.streaming](ctslicingmanager/appcategory/streaming.md)
  An application category for audio and video streaming services.
### Category information
- [var description: String](ctslicingmanager/appcategory/description.md)
  A string representation of the application category.
### Enumeration Cases
- [CTSlicingManager.AppCategory.missionCritical](ctslicingmanager/appcategory/missioncritical.md)
  An application category for mission-critical applications requiring guaranteed reliability.
### Type Properties
- [static var allCases: [CTSlicingManager.AppCategory]](ctslicingmanager/appcategory/allcases.md)
  All application categories supported at the current OS version.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/appcategory)*