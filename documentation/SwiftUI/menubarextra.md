# MenuBarExtra

**Framework**: SwiftUI  
**Kind**: struct

A scene that renders itself as a persistent control in the system menu bar.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct MenuBarExtra<Label, Content> where Label : View, Content : View
```

#### Overview

Use a `MenuBarExtra` when you want to provide access to commonly used functionality, even when your app is not active.

```swift
@main
struct AppWithMenuBarExtra: App {
    @AppStorage("showMenuBarExtra") private var showMenuBarExtra = true

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        MenuBarExtra(
            "App Menu Bar Extra", systemImage: "star",
            isInserted: $showMenuBarExtra)
        {
            StatusMenu()
        }
    }
}
```

Or alternatively, to create a utility app that only shows in the menu bar.

```swift
@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("Utility App", systemImage: "hammer") {
            AppMenu()
        }
    }
}
```

An app that only shows in the menu bar will be automatically terminated if the user removes the extra from the menu bar.

For apps that only show in the menu bar, a common behavior is for the app to not display its icon in either the Dock or the application switcher. To enable this behavior, set the [`LSUIElement`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSUIElement) flag in your app’s [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) file to `true`.

For more complex or data rich menu bar extras, you can use the [`window`](menubarextrastyle/window.md) style, which displays a popover-like window from the menu bar icon that contains standard controls. You define the layout and contents of those controls with the content that you provide:

```swift
MenuBarExtra("Utility App", systemImage: "hammer") {
    ScrollView {
        LazyVGrid(...)
    }
}
.menuBarExtraStyle(.window)
```

## Topics

### Creating a menu bar extra
- [init(_:content:)](menubarextra/init(_:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The extra defines the primary scene of an `App`.
- [init(content: () -> Content, label: () -> Label)](menubarextra/init(content:label:).md)
  Creates a menu bar extra that will be displayed in the system menu bar, and defines the primary scene of an `App`.
- [init(_:isInserted:content:)](menubarextra/init(_:isinserted:content:).md)
  Creates a menu bar extra with a key for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
- [init(isInserted: Binding<Bool>, content: () -> Content, label: () -> Label)](menubarextra/init(isinserted:content:label:).md)
  Creates a menu bar extra. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.
### Creating a menu bar extra with an image
- [init(_:image:content:)](menubarextra/init(_:image:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:image:isInserted:content:)](menubarextra/init(_:image:isinserted:content:).md)
  Creates a menu bar extra with an image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:content:)](menubarextra/init(_:systemimage:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.
- [init(_:systemImage:isInserted:content:)](menubarextra/init(_:systemimage:isinserted:content:).md)
  Creates a menu bar extra with a system image to use as the items label. The provided title will be used by the accessibility system.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [func menuBarExtraStyle<S>(S) -> some Scene](scene/menubarextrastyle(_:).md)
  Sets the style for menu bar extra created by this scene.
- [protocol MenuBarExtraStyle](menubarextrastyle.md)
  A specification for the appearance and behavior of a menu bar extra scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra)*