# init(_:value:total:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<S, V>(_ title: S, value: V?, total: V = 1.0) where Label == Text, CurrentValueLabel == EmptyView, S : StringProtocol, V : BinaryFloatingPoint
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, value: V?, total: V = 1.0) where Label == Text, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings. To initialize a determinate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## Parameters

- `titleResource`: Text resource for the progress view’s localized title that describes the task in progress.
- `value`: The completed amount of the task to this point, in a range of `0.0` to `total`, or `nil` if the progress is indeterminate.
- `total`: The full amount representing the complete scope of the task, meaning the task is complete if `value` equals `total`. The default value is `1.0`.

## See Also

### Creating a determinate progress view
- [init(Progress)](./init%28_%29-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init<V>(value: V?, total: V)](./init%28value,total%29.md)
  Creates a progress view for showing determinate progress.
- [init<V>(value: V?, total: V, label: () -> Label)](./init%28value,total,label%29.md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](./init%28value,total,label,currentvaluelabel%29.md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:value:total:))*