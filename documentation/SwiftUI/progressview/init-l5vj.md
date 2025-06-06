# init(_:)

**Framework**: SwiftUI  
**Kind**: init

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

#### Discussion

The progress view synthesizes a default label using the `localizedDescription` of the given progress instance.

## See Also

- [init<V>(value: V?, total: V)](progressview/init(value:total:).md)
  Creates a progress view for showing determinate progress.
- [init(_:value:total:)](progressview/init(_:value:total:).md)
  Creates a progress view for showing determinate progress that generates its label from a string.
- [init<V>(value: V?, total: V, label: () -> Label)](progressview/init(value:total:label:).md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(value:total:label:currentvaluelabel:).md)
  Creates a progress view for showing determinate progress, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-l5vj)*