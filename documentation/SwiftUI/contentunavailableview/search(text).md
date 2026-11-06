# search(text:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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

Available when `Label` is `SearchUnavailableContent.Label`, `Description` is `SearchUnavailableContent.Description`, and `Actions` is `SearchUnavailableContent.Actions`.

## Discussion

For example, consider the usage of this static member in *ContactsListView*:

```swift
struct ContactsListView: View {
    @State private var searchText = ""
    @State private var searchResults: [Contact] = []

    var body: some View {
        NavigationStack {
            CustomSearchBar(query: $searchText)
            List {
                ForEach(searchResults) { contact in
                    NavigationLink(contact.name, value: contact)
                }
            }
            .navigationDestination(for: Contact.self) { contact in
                ContactsView(contact)
            }
            .navigationTitle("Contacts")
            .overlay {
                if searchResults.isEmpty && !searchText.isEmpty {
                    ContentUnavailableView
                        .search(text: searchText)
                }
            }
            .task(id: searchText) {
                searchResults = await Contact.fetch(searchText)
            }
        }
    }
}
```

## Parameters

- `text`: The search text query.

## See Also

### Getting built-in unavailable views
- [static var search: ContentUnavailableView<SearchUnavailableContent.Label, SearchUnavailableContent.Description, SearchUnavailableContent.Actions>](./search.md)
  Creates a `ContentUnavailableView` instance that conveys a search state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/search(text:))*