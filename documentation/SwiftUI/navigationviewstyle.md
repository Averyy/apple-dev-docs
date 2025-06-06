# NavigationViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and interaction of a navigation view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol NavigationViewStyle
```

## Topics

### Getting built-in navigation view styles
- [static var automatic: DefaultNavigationViewStyle](navigationviewstyle/automatic.md)
  The default navigation view style in the current context of the view being styled.
- [static var columns: ColumnNavigationViewStyle](navigationviewstyle/columns.md)
  A navigation view style represented by a series of views in columns.
- [static var stack: StackNavigationViewStyle](navigationviewstyle/stack.md)
  A navigation view style represented by a view stack that only shows a single top view at a time.
### Supporting types
- [struct DefaultNavigationViewStyle](defaultnavigationviewstyle.md)
  The default navigation view style.
- [struct ColumnNavigationViewStyle](columnnavigationviewstyle.md)
  A navigation view style represented by a series of views in columns.
- [struct StackNavigationViewStyle](stacknavigationviewstyle.md)
  A navigation view style represented by a view stack that only shows a single top view at a time.
- [struct DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md)
  A navigation view style represented by a primary view stack that navigates to a detail view.

## Relationships

### Conforming Types
- [ColumnNavigationViewStyle](columnnavigationviewstyle.md)
- [DefaultNavigationViewStyle](defaultnavigationviewstyle.md)
- [DoubleColumnNavigationViewStyle](doublecolumnnavigationviewstyle.md)
- [StackNavigationViewStyle](stacknavigationviewstyle.md)

## See Also

- [func navigationViewStyle<S>(S) -> some View](view/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationviewstyle)*