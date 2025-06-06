# search(text:)

**Framework**: SwiftUI  
**Kind**: method

Creates a `ContentUnavailableView` instance that conveys a search state.

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
static func search(text: String) -> ContentUnavailableView<Label, Description, Actions>
```

#### Discussion

For example, consider the usage of this static member in :

```swift
struct ContactsListView: View {
    @ObservedObject private var viewModel = ContactsViewModel()

    var body: some View {
        NavigationStack {
            CustomSearchBar(query: $viewModel.searchText)
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
            .overlay {
                if viewModel.searchResults.isEmpty {
                    ContentUnavailableView
                        .search(text: viewModel.searchText)
                }
            }
        }
    }
}
```

## Parameters

- `text`: The search text query.

## See Also

- [static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions>](contentunavailableview/search.md)
  Creates a `ContentUnavailableView` instance that conveys a search state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/search(text:))*