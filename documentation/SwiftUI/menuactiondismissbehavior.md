# MenuActionDismissBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The set of menu dismissal behavior options.

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
struct MenuActionDismissBehavior
```

## Overview

Configure the menu dismissal behavior for a view hierarchy using the [`menuActionDismissBehavior(_:)`](./view/menuactiondismissbehavior%28_%29.md) view modifier.

## Topics

### Getting dismiss behaviors
- [static let automatic: MenuActionDismissBehavior](./menuactiondismissbehavior/automatic.md)
  Use the a dismissal behavior that’s appropriate for the given context.
- [static let disabled: MenuActionDismissBehavior](./menuactiondismissbehavior/disabled.md)
  Never dismiss the presented menu after performing an action.
- [static let enabled: MenuActionDismissBehavior](./menuactiondismissbehavior/enabled.md)
  Always dismiss the presented menu after performing an action.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)

## See Also

### Configuring menu dismissal
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](./view/menuactiondismissbehavior%28_%29.md)
  Tells a menu whether to dismiss after performing an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menuactiondismissbehavior)*