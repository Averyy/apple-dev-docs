# setActivitySummary(_:animated:)

**Framework**: HealthKitUI  
**Kind**: method  
**Role**: Instance Method

Sets the activity summary displayed by the activity ring view.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func setActivitySummary(_ activitySummary: HKActivitySummary?, animated: Bool)
```

```objc
- (void) setActivitySummary:(HKActivitySummary *) activitySummary animated:(BOOL) animated;
```

## Parameters

- `activitySummary`: The new activity summary.
- `animated`: If [`true`](../../Swift/true.md), the change is animated.

## See Also

### Setting the activity summary
- [var activitySummary: HKActivitySummary?](./activitysummary.md)
  The active summary displayed by the activity ring view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkitui/hkactivityringview/setactivitysummary(_:animated:))*