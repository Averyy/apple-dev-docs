# SpringLoadingBehavior

**Framework**: SwiftUI  
**Kind**: struct

The options for controlling the spring loading behavior of views.

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
struct SpringLoadingBehavior
```

#### Overview

Use values of this type with the [`springLoadingBehavior(_:)`](view/springloadingbehavior(_:).md) modifier.

## Topics

### Getting the behaviors
- [static let automatic: SpringLoadingBehavior](springloadingbehavior/automatic.md)
  The automatic spring loading behavior.
- [static let enabled: SpringLoadingBehavior](springloadingbehavior/enabled.md)
  Spring loaded interactions will be enabled for applicable views.
- [static let disabled: SpringLoadingBehavior](springloadingbehavior/disabled.md)
  Spring loaded interactions will be disabled for applicable views.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](view/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [var springLoadingBehavior: SpringLoadingBehavior](environmentvalues/springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/springloadingbehavior)*