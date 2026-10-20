# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a progress view for visualizing the given progress instance.

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
init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView
```

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource) where Label == Text
```

```swift
nonisolated
init(_ configuration: ProgressViewStyleConfiguration) where Label == ProgressViewStyleConfiguration.Label, CurrentValueLabel == ProgressViewStyleConfiguration.CurrentValueLabel
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey) where Label == Text
```

```swift
nonisolated
init<S>(_ title: S) where Label == Text, S : StringProtocol
```

#### Discussion

The progress view synthesizes a default label using the `localizedDescription` of the given progress instance.

## See Also

### Creating a determinate progress view
- [init<V>(value: V?, total: V)](./init%28value,total%29.md)
  Creates a progress view for showing determinate progress.
- [init(_:value:total:)](./init%28_,value,total%29.md)
  Creates a progress view for showing determinate progress that generates its label from a localized string resource.
- [init<V>(value: V?, total: V, label: () -> Label)](./init%28value,total,label%29.md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](./init%28value,total,label,currentvaluelabel%29.md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-l5vj)*