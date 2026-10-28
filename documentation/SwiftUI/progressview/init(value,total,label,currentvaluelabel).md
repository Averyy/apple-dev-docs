# init(value:total:label:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a progress view for showing determinate progress, with a custom label.

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
init<V>(value: V?, total: V = 1.0, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> CurrentValueLabel) where V : BinaryFloatingPoint
```

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to `View`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

## Parameters

- `value`: The completed amount of the task to this point, in a range of `0.0` to `total`, or `nil` if the progress is indeterminate.
- `total`: The full amount representing the complete scope of the task, meaning the task is complete if `value` equals `total`. The default value is `1.0`.
- `label`: A content builder that creates a view that describes the task in progress.
- `currentValueLabel`: A content builder that creates a view that describes the level of completed progress of the task.

## See Also

### Creating a determinate progress view
- [init(Progress)](./init%28_%29-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init<V>(value: V?, total: V)](./init%28value,total%29.md)
  Creates a progress view for showing determinate progress.
- [init(_:value:total:)](./init%28_,value,total%29.md)
  Creates a progress view for showing determinate progress that generates its label from a localized string resource.
- [init<V>(value: V?, total: V, label: () -> Label)](./init%28value,total,label%29.md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(value:total:label:currentvaluelabel:))*