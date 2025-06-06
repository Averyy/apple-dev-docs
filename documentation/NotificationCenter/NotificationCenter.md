# Notification Center

**Framework**: Notification Center  
**Kind**: module

Create and manage widgets for the Today view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+

#### Overview

The Notification Center framework helps you create and manage app extensions that implement Today widgets. The framework provides an API you can use to specify whether a Today widget has content to display, and to customize aspects of its appearance and behavior. In macOS, the Notification Center framework also provides ways to customize the editing and searching experience in a widget.

![Widgets showing weather information in the Today view on iOS and macOS.](https://docs-assets.developer.apple.com/published/e202f58bcb54e62c748ceb590bb16819/media-3039577%402x.png)

## Topics

### Core Widget
- [protocol NCWidgetProviding](ncwidgetproviding.md)
  The interface for customizing the appearance and behavior of a Today widget.
- [class NCWidgetController](ncwidgetcontroller.md)
  An object used to specify whether a Today widget has content to display.
### Search View
- [class NCWidgetSearchViewController](ncwidgetsearchviewcontroller.md)
  An object that provides a default search view within a macOS Today widget.
- [protocol NCWidgetSearchViewDelegate](ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.
### List View
- [class NCWidgetListViewController](ncwidgetlistviewcontroller.md)
  An object that provides a list view for displaying content in a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NotificationCenter)*