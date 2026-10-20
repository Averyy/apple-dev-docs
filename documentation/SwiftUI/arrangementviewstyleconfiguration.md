# ArrangementViewStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The properties of an arrangement view you provide to create a custom style.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct ArrangementViewStyleConfiguration
```

## Topics

### Setting up a configuration
- [var primary: ArrangementViewStyleConfiguration.Primary](./arrangementviewstyleconfiguration/primary-swift.property.md)
  The primary view to lay out in an arrangement view.
- [ArrangementViewStyleConfiguration.Primary](./arrangementviewstyleconfiguration/primary-swift.struct.md)
  A type-erased view of the primary content of an arrangement view.
- [var secondary: ArrangementViewStyleConfiguration.Secondary](./arrangementviewstyleconfiguration/secondary-swift.property.md)
  The secondary view to lay out in an arrangement view.
- [ArrangementViewStyleConfiguration.Secondary](./arrangementviewstyleconfiguration/secondary-swift.struct.md)
  A type-erased view of the secondary content of an arrangement view.

## See Also

### Creating an arrangement view
- [init(primary: () -> Primary, secondary: () -> Secondary)](./arrangementview/init%28primary,secondary%29.md)
  Creates an arrangement view with a primary and secondary view.
- [init(ArrangementViewStyleConfiguration)](./arrangementview/init%28_%29.md)
  Creates an arrangement view from a style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyleconfiguration)*