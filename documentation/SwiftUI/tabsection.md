# TabSection

**Framework**: SwiftUI  
**Kind**: struct

A container that you can use to add hierarchy within a tab view.

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
struct TabSection<Header, Content, Footer, SelectionValue>
```

#### Overview

Use [`TabSection`](tabsection.md) to organize tab content into separate sections. Each section has custom tab content that you provide on a per-instance basis. You can also provide a header for each section.

## Topics

### Creating a tab section
- [init(content:)](tabsection/init(content:).md)
  Creates a section with the provided section content.
- [init(_:content:)](tabsection/init(_:content:).md)
  Creates a section with the provided content.
- [init(content:header:)](tabsection/init(content:header:).md)
  Creates a section with a header and the provided section content.
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
- [struct Tab](tab.md)
  The content for a tab and the tab’s associated tab item in a tab view.
- [struct TabRole](tabrole.md)
  A value that defines the purpose of the tab.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection)*