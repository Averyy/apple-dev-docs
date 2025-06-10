# LayoutDirection

**Framework**: SwiftUI  
**Kind**: enum

A direction in which SwiftUI can lay out content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum LayoutDirection
```

#### Overview

SwiftUI supports both left-to-right and right-to-left directions for laying out content to support different languages and locales. The system sets the value based on the user’s locale, but you can also use the [`environment(_:_:)`](view/environment(_:_:).md) modifier to override the direction for a view and its child views:

```swift
MyView()
    .environment(\.layoutDirection, .rightToLeft)
```

You can also read the [`layoutDirection`](environmentvalues/layoutdirection.md) environment value to find out which direction applies to a particular environment. However, in many cases, you don’t need to take any action based on this value. SwiftUI horizontally flips the x position of each view within its parent, so layout calculations automatically produce the desired effect for both modes without any changes.

## Topics

### Getting layout directions
- [LayoutDirection.leftToRight](layoutdirection/lefttoright.md)
  A left-to-right layout direction.
- [LayoutDirection.rightToLeft](layoutdirection/righttoleft.md)
  A right-to-left layout direction.
### Creating a layout direction
- [init?(UITraitEnvironmentLayoutDirection)](layoutdirection/init(_:).md)
  Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](view/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [enum LayoutDirectionBehavior](layoutdirectionbehavior.md)
  A description of what should happen when the layout direction changes.
- [var layoutDirection: LayoutDirection](environmentvalues/layoutdirection.md)
  The layout direction associated with the current environment.
- [struct LayoutRotationUnaryLayout](layoutrotationunarylayout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutdirection)*