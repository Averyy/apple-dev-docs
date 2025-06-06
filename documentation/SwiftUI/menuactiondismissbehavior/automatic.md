# automatic

**Framework**: SwiftUI  
**Kind**: property

Use the a dismissal behavior that’s appropriate for the given context.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static let automatic: MenuActionDismissBehavior
```

#### Discussion

In most cases, the default behavior is [`enabled`](menuactiondismissbehavior/enabled.md). There are some cases, like [`Stepper`](stepper.md), that use [`disabled`](menuactiondismissbehavior/disabled.md) by default.

## See Also

- [static let disabled: MenuActionDismissBehavior](menuactiondismissbehavior/disabled.md)
  Never dismiss the presented menu after performing an action.
- [static let enabled: MenuActionDismissBehavior](menuactiondismissbehavior/enabled.md)
  Always dismiss the presented menu after performing an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menuactiondismissbehavior/automatic)*