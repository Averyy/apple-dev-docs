# ContentUnavailableView

**Framework**: SwiftUI  
**Kind**: struct

An interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ContentUnavailableView<Label, Description, Actions> where Label : View, Description : View, Actions : View
```

#### Overview

It is recommended to use `ContentUnavailableView` in situations where a view’s content cannot be displayed. That could be caused by a network error, a list without items, a search that returns no results etc.

You create an `ContentUnavailableView` in its simplest form, by providing a label and some additional content such as a description or a call to action:

```swift
ContentUnavailableView {
    Label("No Mail", systemImage: "tray.fill")
} description: {
    Text("New mails you receive will appear here.")
}
```

The system provides default `ContentUnavailableView`s that you can use in specific situations. The example below illustrates the usage of the [`search`](contentunavailableview/search.md) view:

```swift
struct ContentView: View {
    @ObservedObject private var viewModel = ContactsViewModel()

    var body: some View {
        NavigationStack {
            List {
                ForEach(viewModel.searchResults) { contact in
                    NavigationLink {
                        ContactsView(contact)
                    } label: {
                        Text(contact.name)
                    }
                }
            }
            .navigationTitle("Contacts")
            .searchable(text: $viewModel.searchText)
            .overlay {
                if searchResults.isEmpty {
                    ContentUnavailableView.search
                }
            }
        }
    }
}
```

## Topics

### Getting built-in unavailable views
- [static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions>](contentunavailableview/search.md)
  Creates a `ContentUnavailableView` instance that conveys a search state.
- [static func search(text: String) -> ContentUnavailableView<Label, Description, Actions>](contentunavailableview/search(text:).md)
  Creates a `ContentUnavailableView` instance that conveys a search state.
### Creating an unavailable view
- [init(label: () -> Label, description: () -> Description, actions: () -> Actions)](contentunavailableview/init(label:description:actions:).md)
  Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.
- [init(_:image:description:)](contentunavailableview/init(_:image:description:).md)
  Creates an interface, consisting of a title generated from a localized string, an image and additional content, that you display when the content of your app is unavailable to users.
- [init(_:systemImage:description:)](contentunavailableview/init(_:systemimage:description:).md)
  Creates an interface, consisting of a title generated from a localized string, a system icon image and additional content, that you display when the content of your app is unavailable to users.
### Supporting types
- [struct SearchUnavailableContent](searchunavailablecontent.md)
  A structure that represents the body of a static placeholder search view.

## Relationships

### Conforms To
- [View](view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview)*