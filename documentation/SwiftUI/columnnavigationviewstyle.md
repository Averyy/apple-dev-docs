# ColumnNavigationViewStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A navigation view style represented by a series of views in columns.

**Availability**:
- iOS 15.0+ - Deprecated in 27.2
- iPadOS 15.0+ - Deprecated in 27.2
- Mac Catalyst 15.0+ - Deprecated in 27.2
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](./navigationview.md) with a [`NavigationStack`](./navigationstack.md) or [`NavigationSplitView`](./navigationsplitview.md). For more information, see [Migrating to new navigation types](./migrating-to-new-navigation-types.md).

## Declaration

```swift
struct ColumnNavigationViewStyle
```

## Overview

Use [`columns`](./navigationviewstyle/columns.md) to construct this style.

## Relationships

### Conforms To
- [NavigationViewStyle](./navigationviewstyle.md)

## See Also

### Supporting types
- [struct DefaultNavigationViewStyle](./defaultnavigationviewstyle.md)
  The default navigation view style.
- [struct StackNavigationViewStyle](./stacknavigationviewstyle.md)
  A navigation view style represented by a view stack that only shows a single top view at a time.
- [struct DoubleColumnNavigationViewStyle](./doublecolumnnavigationviewstyle.md)
  A navigation view style represented by a primary view stack that navigates to a detail view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/columnnavigationviewstyle)*