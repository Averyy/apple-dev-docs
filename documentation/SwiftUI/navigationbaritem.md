# NavigationBarItem

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A configuration for a navigation bar that represents a view at the top of a navigation stack.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct NavigationBarItem
```

## Overview

Use one of the [`NavigationBarItem.TitleDisplayMode`](./navigationbaritem/titledisplaymode.md) values to configure a navigation bar title’s display mode with the [`navigationBarTitleDisplayMode(_:)`](./view/navigationbartitledisplaymode%28_%29.md) view modifier.

## Topics

### Setting a title display mode
- [NavigationBarItem.TitleDisplayMode](./navigationbaritem/titledisplaymode.md)
  A style for displaying the title of a navigation bar.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the navigation bar
- [func navigationBarBackButtonHidden(Bool) -> some View](./view/navigationbarbackbuttonhidden%28_%29.md)
  Hides the navigation bar back button for the view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](./view/navigationbartitledisplaymode%28_%29.md)
  Configures the title display mode for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationbaritem)*