# init(value:total:label:)

**Framework**: SwiftUI  
**Kind**: init

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
init<V>(value: V?, total: V = 1.0, @ViewBuilder label: () -> Label) where CurrentValueLabel == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

## Parameters

- `value`: The completed amount of the task to this point, in a range   of   to  , or   if the progress is indeterminate.
- `total`: The full amount representing the complete scope of the   task, meaning the task is complete if   equals  . The   default value is  .
- `label`: A view builder that creates a view that describes the task   in progress.

## See Also

- [init(Progress)](progressview/init(_:)-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init<V>(value: V?, total: V)](progressview/init(value:total:).md)
  Creates a progress view for showing determinate progress.
- [init(_:value:total:)](progressview/init(_:value:total:).md)
  Creates a progress view for showing determinate progress that generates its label from a string.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(value:total:label:currentvaluelabel:).md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(value:total:label:))*