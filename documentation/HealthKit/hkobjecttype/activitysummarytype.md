# activitySummaryType()

**Framework**: HealthKit  
**Kind**: method

Returns the shared activity summary type.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
class func activitySummaryType() -> HKActivitySummaryType
```

#### Return Value

The shared [`HKActivitySummaryType`](hkactivitysummarytype.md) instance.

#### Discussion

This method returns an instance of the [`HKActivitySummaryType`](hkactivitysummarytype.md) concrete subclass. Use this type to request permission to read [`HKActivitySummary`](hkactivitysummary.md) objects from the HealthKit store.

> **Note**:  You cannot request permission to share [`HKActivitySummary`](hkactivitysummary.md) objects.

 You cannot request permission to share [`HKActivitySummary`](hkactivitysummary.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/activitysummarytype())*