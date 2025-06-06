# ToolbarTitleMenu

**Framework**: SwiftUI  
**Kind**: struct

The title menu of a toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ToolbarTitleMenu<Content> where Content : View
```

#### Overview

A title menu represents common functionality that can be done on the content represented by your app’s toolbar or navigation title. This menu may be populated from your app’s commands like [`saveItem`](commandgroupplacement/saveitem.md) or [`printItem`](commandgroupplacement/printitem.md).

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu()
    }
```

You can provide your own set of actions to override this behavior.

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu {
            DuplicateButton()
            PrintButton()
        }
    }
```

In iOS and iPadOS, this will construct a menu that can be presented by tapping the navigation title in the app’s navigation bar.

## Topics

### Creating a toolbar title menu
- [init()](toolbartitlemenu/init.md)
  Creates a toolbar title menu where actions are inferred from your apps commands.
- [init(content: () -> Content)](toolbartitlemenu/init(content:).md)
  Creates a toolbar title menu.

## Relationships

### Conforms To
- [CustomizableToolbarContent](customizabletoolbarcontent.md)
- [ToolbarContent](toolbarcontent.md)

## See Also

- [func toolbarTitleMenu<C>(content: () -> C) -> some View](view/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbartitlemenu)*