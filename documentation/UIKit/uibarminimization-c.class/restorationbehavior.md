# restorationBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The restoration behavior.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (nonatomic, assign) UIBarMinimizationRestorationBehavior restorationBehavior;
```

## Discussion

Use this property alongside [`minimizationBehavior`](./minimizationbehavior.md) to control when a minimized navigation bar restores. By default the bar restores when the user reverses scroll direction; with `UIBarMinimizationRestorationBehaviorAtScrollEdge`, the bar instead restores only when the scroll view’s content reaches the scroll edge. Currently only honored in combination with `UIBarMinimizationBehaviorOnScrollDown`.

The default value is `UIBarMinimizationRestorationBehaviorAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimization-c.class/restorationbehavior)*