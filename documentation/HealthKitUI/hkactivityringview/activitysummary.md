# activitySummary

**Framework**: HealthKitUI  
**Kind**: property  
**Role**: Instance Property

The active summary displayed by the activity ring view.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var activitySummary: HKActivitySummary? { get set }
```

```objc
@property (nonatomic, strong, nullable) HKActivitySummary * activitySummary;
```

## Discussion

Any changes made directly to this property are not animated. To animate changes, use # [`setActivitySummary(_:animated:)`](./setactivitysummary%28_,animated%29.md) instead.

## See Also

### Setting the activity summary
- [func setActivitySummary(HKActivitySummary?, animated: Bool)](./setactivitysummary%28_,animated%29.md)
  Sets the activity summary displayed by the activity ring view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkitui/hkactivityringview/activitysummary)*