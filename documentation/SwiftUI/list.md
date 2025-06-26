# List

**Framework**: SwiftUI  
**Kind**: struct

A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency struct List<SelectionValue, Content> where SelectionValue : Hashable, Content : View
```

## Mentions

- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Performing a search operation](performing-a-search-operation.md)
- [Migrating to new navigation types](migrating-to-new-navigation-types.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)

#### Overview

In its simplest form, a `List` creates its contents statically, as shown in the following example:

```swift
var body: some View {
    List {
        Text("A List Item")
        Text("A Second List Item")
        Text("A Third List Item")
    }
}
```

![A vertical list with three text views.](https://docs-assets.developer.apple.com/published/d78009ccd78b71238938528c05b70d1c/List-1-iOS%402x.png)

More commonly, you create lists dynamically from an underlying collection of data. The following example shows how to create a simple list from an array of an `Ocean` type which conforms to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable):

```swift
struct Ocean: Identifiable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

var body: some View {
    List(oceans) {
        Text($0.name)
    }
}
```

![A vertical list with five text views, each with the name of an](https://docs-assets.developer.apple.com/published/a77e63fad0ed8d8fa53ef462fe01e2a6/List-2-iOS%402x.png)

##### Supporting Selection in Lists

To make members of a list selectable, provide a binding to a selection variable. Binding to a single instance of the list data’s `Identifiable.ID` type creates a single-selection list. Binding to a [`Set`](https://developer.apple.com/documentation/Swift/Set) creates a list that supports multiple selections. The following example shows how to add multiselect to the previous example:

```swift
struct Ocean: Identifiable, Hashable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

@State private var multiSelection = Set<UUID>()

var body: some View {
    NavigationView {
        List(oceans, selection: $multiSelection) {
            Text($0.name)
        }
        .navigationTitle("Oceans")
        .toolbar { EditButton() }
    }
    Text("\(multiSelection.count) selections")
}
```

When people make a single selection by tapping or clicking, the selected cell changes its appearance to indicate the selection. To enable multiple selections with tap gestures, put the list into edit mode by either modifying the [`editMode`](environmentvalues/editmode.md) value, or adding an [`EditButton`](editbutton.md) to your app’s interface. When you put the list into edit mode, the list shows a circle next to each list item. The circle contains a checkmark when the user selects the associated item. The example above uses an Edit button, which changes its title to Done while in edit mode:

![A navigation view with the title Oceans and a vertical list that contains](https://docs-assets.developer.apple.com/published/949b2bed10274ec967fa27a113020e9b/List-3-iOS%402x.png)

People can make multiple selections without needing to enter edit mode on devices that have a keyboard and mouse or trackpad, like Mac and iPad.

##### Refreshing the List Content

To make the content of the list refreshable using the standard refresh control, use the [`refreshable(action:)`](view/refreshable(action:).md) modifier.

The following example shows how to add a standard refresh control to a list. When the user drags the top of the list downward, SwiftUI reveals the refresh control and executes the specified action. Use an `await` expression inside the `action` closure to refresh your data. The refresh indicator remains visible for the duration of the awaited operation.

```swift
struct Ocean: Identifiable, Hashable {
     let name: String
     let id = UUID()
     let stats: [String: String]
 }

 class OceanStore: ObservableObject {
     @Published var oceans = [Ocean]()
     func loadStats() async {}
 }

 @EnvironmentObject var store: OceanStore

 var body: some View {
     NavigationView {
         List(store.oceans) { ocean in
             HStack {
                 Text(ocean.name)
                 StatsSummary(stats: ocean.stats) // A custom view for showing statistics.
             }
         }
         .refreshable {
             await store.loadStats()
         }
         .navigationTitle("Oceans")
     }
 }
```

##### Supporting Multidimensional Lists

To create two-dimensional lists, group items inside [`Section`](section.md) instances. The following example creates sections named after the world’s oceans, each of which has [`Text`](text.md) views named for major seas attached to those oceans. The example also allows for selection of a single list item, identified by the `id` of the example’s `Sea` type.

```swift
struct ContentView: View {
    struct Sea: Hashable, Identifiable {
        let name: String
        let id = UUID()
    }

    struct OceanRegion: Identifiable {
        let name: String
        let seas: [Sea]
        let id = UUID()
    }

    private let oceanRegions: [OceanRegion] = [
        OceanRegion(name: "Pacific",
                    seas: [Sea(name: "Australasian Mediterranean"),
                           Sea(name: "Philippine"),
                           Sea(name: "Coral"),
                           Sea(name: "South China")]),
        OceanRegion(name: "Atlantic",
                    seas: [Sea(name: "American Mediterranean"),
                           Sea(name: "Sargasso"),
                           Sea(name: "Caribbean")]),
        OceanRegion(name: "Indian",
                    seas: [Sea(name: "Bay of Bengal")]),
        OceanRegion(name: "Southern",
                    seas: [Sea(name: "Weddell")]),
        OceanRegion(name: "Arctic",
                    seas: [Sea(name: "Greenland")])
    ]

    @State private var singleSelection: UUID?

    var body: some View {
        NavigationView {
            List(selection: $singleSelection) {
                ForEach(oceanRegions) { region in
                    Section(header: Text("Major \(region.name) Ocean Seas")) {
                        ForEach(region.seas) { sea in
                            Text(sea.name)
                        }
                    }
                }
            }
            .navigationTitle("Oceans and Seas")
        }
    }
}
```

Because this example uses single selection, people can make selections outside of edit mode on all platforms.

![A vertical list split into sections titled Major Pacific Ocean Seas,](https://docs-assets.developer.apple.com/published/6bcb184683b070eed33ede7aa2775cea/List-4-iOS%402x.png)

> **Note**: In iOS 15, iPadOS 15, and tvOS 15 and earlier, lists support selection only in edit mode, even for single selections.

##### Creating Hierarchical Lists

You can also create a hierarchical list of arbitrary depth by providing tree-structured data and a `children` parameter that provides a key path to get the child nodes at any level. The following example uses a deeply-nested collection of a custom `FileItem` type to simulate the contents of a file system. The list created from this data uses collapsing cells to allow the user to navigate the tree structure.

```swift
struct ContentView: View {
    struct FileItem: Hashable, Identifiable, CustomStringConvertible {
        var id: Self { self }
        var name: String
        var children: [FileItem]? = nil
        var description: String {
            switch children {
            case nil:
                return "📄 \(name)"
            case .some(let children):
                return children.isEmpty ? "📂 \(name)" : "📁 \(name)"
            }
        }
    }
    let fileHierarchyData: [FileItem] = [
      FileItem(name: "users", children:
        [FileItem(name: "user1234", children:
          [FileItem(name: "Photos", children:
            [FileItem(name: "photo001.jpg"),
             FileItem(name: "photo002.jpg")]),
           FileItem(name: "Movies", children:
             [FileItem(name: "movie001.mp4")]),
              FileItem(name: "Documents", children: [])
          ]),
         FileItem(name: "newuser", children:
           [FileItem(name: "Documents", children: [])
           ])
        ]),
        FileItem(name: "private", children: nil)
    ]
    var body: some View {
        List(fileHierarchyData, children: \.children) { item in
            Text(item.description)
        }
    }
}
```

![A list providing an expanded view of a tree structure. Some rows have a](https://docs-assets.developer.apple.com/published/be9c84b8dbaf63becfdaed28332a89e0/List-5-iOS%402x.png)

##### Styling Lists

SwiftUI chooses a display style for a list based on the platform and the view type in which it appears. Use the [`listStyle(_:)`](view/liststyle(_:).md) modifier to apply a different [`ListStyle`](liststyle.md) to all lists within a view. For example, adding `.listStyle(.plain)` to the example shown in the “Creating Multidimensional Lists” topic applies the [`plain`](liststyle/plain.md) style, the following screenshot shows:

![A vertical list split into sections titled Major Pacific Ocean Seas,](https://docs-assets.developer.apple.com/published/d1d46ab3e64ce8b26d1fe9a61ea3ffa5/List-6-iOS%402x.png)

## Topics

### Creating a list from a set of views
- [init(content: () -> Content)](list/init(content:).md)
  Creates a list with the given content.
- [init(selection:content:)](list/init(selection:content:).md)
  Creates a list with the given content that supports selecting a single row that cannot be deselcted.
### Creating a list from enumerated data
- [init(_:rowContent:)](list/init(_:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:selection:rowContent:)](list/init(_:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](list/init(_:id:rowcontent:).md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](list/init(_:id:selection:rowcontent:).md)
  Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.
### Creating a list from hierarchical data
- [init(_:children:rowContent:)](list/init(_:children:rowcontent:).md)
  Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data.
- [init(_:children:selection:rowContent:)](list/init(_:children:selection:rowcontent:).md)
  Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data and allowing users to have exactly one row always selected.
- [init(_:id:children:rowContent:)](list/init(_:id:children:rowcontent:).md)
  Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:children:selection:rowContent:)](list/init(_:id:children:selection:rowcontent:).md)
  Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data and allowing users to have exactly one row always selected.
### Creating a list from editable data
- [init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](list/init(_:editactions:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.
- [init(_:editActions:selection:rowContent:)](list/init(_:editactions:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data, allows to edit the collection, and requires a selection of a single row.
- [init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) -> RowContent)](list/init(_:id:editactions:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable data and allows to edit the collection.
- [init(_:id:editActions:selection:rowContent:)](list/init(_:id:editactions:selection:rowcontent:).md)
  Creates a list that computes its rows on demand from an underlying collection of identifiable, allows to edit the collection, and requires a selection of a single row.
### Supporting types
- [var body: some View](list/body.md)
  The content of the list.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Displaying data in lists](displaying-data-in-lists.md)
  Visualize collections of data with platform-appropriate appearance.
- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list)*