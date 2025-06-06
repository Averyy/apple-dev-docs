# ControlSize

**Framework**: SwiftUI  
**Kind**: enum

The size classes, like regular or small, that you can apply to controls within a view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum ControlSize
```

## Topics

### Getting control sizes
- [ControlSize.mini](controlsize/mini.md)
  A control version that is minimally sized.
- [ControlSize.small](controlsize/small.md)
  A control version that is proportionally smaller size for space-constrained views.
- [ControlSize.regular](controlsize/regular.md)
  A control version that is the default size.
- [ControlSize.large](controlsize/large.md)
  A control version that is prominently sized.
- [ControlSize.extraLarge](controlsize/extralarge.md)
  A control version that is substantially sized. The largest control size. Resolves to [`ControlSize.large`](controlsize/large.md) on platforms other than visionOS.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func controlSize(ControlSize) -> some View](view/controlsize(_:).md)
  Sets the size for controls within this view.
- [var controlSize: ControlSize](environmentvalues/controlsize.md)
  The size to apply to controls within a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlsize)*