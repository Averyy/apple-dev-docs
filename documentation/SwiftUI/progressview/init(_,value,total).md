# init(_:value:total:)

**Framework**: SwiftUI  
**Kind**: init

Creates a progress view for showing determinate progress that generates its label from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: V?, total: V = 1.0) where Label == Text, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings. To initialize a determinate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## Parameters

- `titleResource`: Text resource for the progress view’s localized title that describes the task in progress.
- `value`: The completed amount of the task to this point, in a range of `0.0` to `total`, or `nil` if the progress is indeterminate.
- `total`: The full amount representing the complete scope of the task, meaning the task is complete if `value` equals `total`. The default value is `1.0`.

## See Also

- [init(Progress)](progressview/init(_:)-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init<V>(value: V?, total: V)](progressview/init(value:total:).md)
  Creates a progress view for showing determinate progress.
- [init<V>(value: V?, total: V, label: () -> Label)](progressview/init(value:total:label:).md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(value:total:label:currentvaluelabel:).md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:value:total:))*