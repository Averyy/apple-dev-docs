# StackNavigationViewStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A navigation view style represented by a view stack that only shows a single top view at a time.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](./navigationview.md) with a [`NavigationStack`](./navigationstack.md) or [`NavigationSplitView`](./navigationsplitview.md). For more information, see [Migrating to new navigation types](./migrating-to-new-navigation-types.md).

## Declaration

```swift
struct StackNavigationViewStyle
```

#### Overview

Use [`stack`](./navigationviewstyle/stack.md) to construct this style.

## Topics

### Creating a stack navigation view style
- [init()](./stacknavigationviewstyle/init%28%29.md)
  Creates a navigation view style represented by a view stack that only shows a single top view at a time.

## Relationships

### Conforms To
- [NavigationViewStyle](./navigationviewstyle.md)

## See Also

### Supporting types
- [struct DefaultNavigationViewStyle](./defaultnavigationviewstyle.md)
  The default navigation view style.
- [struct ColumnNavigationViewStyle](./columnnavigationviewstyle.md)
  A navigation view style represented by a series of views in columns.
- [struct DoubleColumnNavigationViewStyle](./doublecolumnnavigationviewstyle.md)
  A navigation view style represented by a primary view stack that navigates to a detail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stacknavigationviewstyle)*