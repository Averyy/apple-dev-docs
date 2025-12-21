# Tab

**Framework**: SwiftUI  
**Kind**: struct

The content for a tab and the tab’s associated tab item in a tab view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Tab<Value, Content, Label>
```

## Topics

### Creating a tab
- [init(content: () -> Content)](tab/init(content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:content:)](tab/init(value:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(role: TabRole?, content: () -> Content)](tab/init(role:content:).md)
  Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](tab/init(value:role:content:).md)
  Creates a new tab with a label inferred from the role.
### Creating a tab with label
- [init(content: () -> Content, label: () -> Label)](tab/init(content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
- [init(value:content:label:)](tab/init(value:content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
- [init(role: TabRole?, content: () -> Content, label: () -> Label)](tab/init(role:content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](tab/init(value:role:content:label:).md)
  Creates a new tab with a label that you can use in a tab view.
### Creating a tab with system symbol
- [init(_:systemImage:content:)](tab/init(_:systemimage:content:).md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:content:)](tab/init(_:systemimage:value:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
- [init(_:systemImage:role:content:)](tab/init(_:systemimage:role:content:).md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:role:content:)](tab/init(_:systemimage:value:role:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
### Creating a tab with image
- [init(_:image:content:)](tab/init(_:image:content:).md)
  Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:content:)](tab/init(_:image:value:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
- [init(_:image:role:content:)](tab/init(_:image:role:content:).md)
  Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:role:content:)](tab/init(_:image:value:role:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
### Supporting types
- [struct DefaultTabLabel](defaulttablabel.md)
  The default label to use for a tab or tab section.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [TabContent](tabcontent.md)

## See Also

- [Enhancing your app’s content with tab navigation](enhancing-your-app-content-with-tab-navigation.md)
  Keep your app content front and center while providing quick access to navigation using the tab bar.
- [struct TabView](tabview.md)
  A view that switches between multiple child views using interactive user interface elements.
- [struct TabRole](tabrole.md)
  A value that defines the purpose of the tab.
- [struct TabSection](tabsection.md)
  A container that you can use to add hierarchy within a tab view.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab)*