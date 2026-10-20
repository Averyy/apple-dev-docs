# init(value:total:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a progress view for showing determinate progress.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init<V>(value: V?, total: V = 1.0) where Label == EmptyView, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint
```

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to `View`.

#### Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

## Parameters

- `value`: The completed amount of the task to this point, in a range of `0.0` to `total`, or `nil` if the progress is indeterminate.
- `total`: The full amount representing the complete scope of the task, meaning the task is complete if `value` equals `total`. The default value is `1.0`.

## See Also

### Creating a determinate progress view
- [init(Progress)](./init%28_%29-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init(_:value:total:)](./init%28_,value,total%29.md)
  Creates a progress view for showing determinate progress that generates its label from a localized string resource.
- [init<V>(value: V?, total: V, label: () -> Label)](./init%28value,total,label%29.md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](./init%28value,total,label,currentvaluelabel%29.md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(value:total:))*