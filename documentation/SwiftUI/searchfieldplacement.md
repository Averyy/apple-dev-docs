# SearchFieldPlacement

**Framework**: SwiftUI  
**Kind**: struct

The placement of a search field in a view hierarchy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SearchFieldPlacement
```

## Mentions

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)

#### Overview

You can give a preferred placement to any of the searchable modifiers, like [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md):

```swift
var body: some View {
    NavigationView {
        PrimaryView()
        SecondaryView()
        Text("Select a primary and secondary item")
    }
    .searchable(text: $text, placement: .sidebar)
}
```

Depending on the containing view hierachy, SwiftUI might not be able to fulfill your request.

## Topics

### Getting a search field placement
- [static let automatic: SearchFieldPlacement](searchfieldplacement/automatic.md)
  SwiftUI places the search field automatically.
- [static let navigationBarDrawer: SearchFieldPlacement](searchfieldplacement/navigationbardrawer.md)
  The search field appears in the navigation bar.
- [static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement](searchfieldplacement/navigationbardrawer(displaymode:).md)
  The search field appears in the navigation bar using the specified display mode.
- [static let sidebar: SearchFieldPlacement](searchfieldplacement/sidebar.md)
  The search field appears in the sidebar of a navigation view.
- [static let toolbar: SearchFieldPlacement](searchfieldplacement/toolbar.md)
  The search field appears in the toolbar.
### Supporting types
- [SearchFieldPlacement.NavigationBarDrawerDisplayMode](searchfieldplacement/navigationbardrawerdisplaymode.md)
  A mode that determines when to display a search field that appears in a navigation bar.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)
  Present an interface that people can use to search for content in your app.
- [Performing a search operation](performing-a-search-operation.md)
  Update search results based on search text and optional tokens that you store.
- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:tokens:placement:prompt:token:)](view/searchable(text:tokens:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens.
- [func searchable(text:editableTokens:placement:prompt:token:)](view/searchable(text:editabletokens:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement)*