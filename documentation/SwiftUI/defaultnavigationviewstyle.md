# DefaultNavigationViewStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The default navigation view style.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](./navigationview.md) with a [`NavigationStack`](./navigationstack.md) or [`NavigationSplitView`](./navigationsplitview.md). For more information, see [Migrating to new navigation types](./migrating-to-new-navigation-types.md).

## Declaration

```swift
struct DefaultNavigationViewStyle
```

#### Overview

Use [`automatic`](./navigationviewstyle/automatic.md) to construct this style.

## Topics

### Creating a default navigation view style
- [init()](./defaultnavigationviewstyle/init%28%29.md)
  Creates the default navigation view style.

## Relationships

### Conforms To
- [NavigationViewStyle](./navigationviewstyle.md)

## See Also

### Supporting types
- [struct ColumnNavigationViewStyle](./columnnavigationviewstyle.md)
  A navigation view style represented by a series of views in columns.
- [struct StackNavigationViewStyle](./stacknavigationviewstyle.md)
  A navigation view style represented by a view stack that only shows a single top view at a time.
- [struct DoubleColumnNavigationViewStyle](./doublecolumnnavigationviewstyle.md)
  A navigation view style represented by a primary view stack that navigates to a detail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaultnavigationviewstyle)*