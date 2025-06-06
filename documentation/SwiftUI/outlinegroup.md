# OutlineGroup

**Framework**: SwiftUI  
**Kind**: struct

A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable
```

## Mentions

- [Displaying data in lists](displaying-data-in-lists.md)

#### Overview

Use an outline group when you need a view that can represent a hierarchy of data by using disclosure views. This allows the user to navigate the tree structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a simplified view of a file system. Passing the root of this tree and the key path of its children allows you to quickly create a visual representation of the file system.

```swift
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

let data =
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
    ])

OutlineGroup(data, children: \.children) { item in
    Text("\(item.description)")
}
```

##### Type Parameters

Five generic type constraints define a specific `OutlineGroup` instance:

- `Data`: The type of a collection containing the children of an element in the tree-shaped data.
- `ID`: The type of the identifier for an element.
- `Parent`: The type of the visual representation of an element whose children property is non-`nil`
- `Leaf`: The type of the visual representation of an element whose children property is `nil`.
- `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

## Topics

### Creating an outline group
- [init(_:children:)](outlinegroup/init(_:children:).md)
  Creates an outline group from a collection of root data elements and a key path to element’s children.
- [init(_:children:content:)](outlinegroup/init(_:children:content:).md)
  Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](outlinegroup/init(_:id:children:content:).md)
  Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.
### Supporting types
- [struct OutlineSubgroupChildren](outlinesubgroupchildren.md)
  A type-erased view representing the children in an outline subgroup.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [TableRowContent](tablerowcontent.md)
- [View](view.md)

## See Also

- [struct DisclosureGroup](disclosuregroup.md)
  A view that shows or hides another content view, based on the state of a disclosure control.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/outlinegroup)*