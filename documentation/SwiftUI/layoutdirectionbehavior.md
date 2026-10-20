# LayoutDirectionBehavior

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

A description of what should happen when the layout direction changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum LayoutDirectionBehavior
```

#### Overview

A `LayoutDirectionBehavior` can be used with the `layoutDirectionBehavior` view modifier or the `layoutDirectionBehavior` property of `Shape`.

## Topics

### Getting behaviors
- [LayoutDirectionBehavior.fixed](./layoutdirectionbehavior/fixed.md)
  A behavior that doesn’t mirror when the layout direction changes.
- [static var mirrors: LayoutDirectionBehavior](./layoutdirectionbehavior/mirrors.md)
  A behavior that mirrors when the layout direction is right-to-left.
- [LayoutDirectionBehavior.mirrors(in:)](./layoutdirectionbehavior/mirrors%28in%29.md)
  A behavior that mirrors when the layout direction has the specified value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting a layout direction
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](./view/layoutdirectionbehavior%28_%29.md)
  Sets the behavior of this view for different layout directions.
- [var layoutDirection: LayoutDirection](./environmentvalues/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum LayoutDirection](./layoutdirection.md)
  A direction in which SwiftUI can lay out content.
- [struct LayoutRotationUnaryLayout](./layoutrotationunarylayout.md)
  A layout that rotates the space containing a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutdirectionbehavior)*