# ForEach

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A structure that computes views on demand from an underlying collection of identified data.

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
struct ForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable
```

## Mentions

- [Creating performant scrollable stacks](./creating-performant-scrollable-stacks.md)
- [Displaying data in lists](./displaying-data-in-lists.md)
- [Grouping data with lazy stack views](./grouping-data-with-lazy-stack-views.md)
- [Reordering items in lists, stacks, grids, and custom layouts](./reordering-items-in-lists-stacks-grids-and-custom-layouts.md)
- [Picking container views for your content](./picking-container-views-for-your-content.md)

## Overview

Use `ForEach` to provide views based on a [`RandomAccessCollection`](../Swift/randomaccesscollection.md) of some data type. Either the collection’s elements must conform to [`Identifiable`](../Swift/identifiable.md) or you need to provide an `id` parameter to the `ForEach` initializer.

The following example creates a `NamedFont` type that conforms to [`Identifiable`](../Swift/identifiable.md), and an array of this type called `namedFonts`. A `ForEach` instance iterates over the array, producing new [`Text`](./text.md) instances that display examples of each SwiftUI [`Font`](./font.md) style provided in the array.

```swift
private struct NamedFont: Identifiable {
    let name: String
    let font: Font
    var id: String { name }
}

private let namedFonts: [NamedFont] = [
    NamedFont(name: "Large Title", font: .largeTitle),
    NamedFont(name: "Title", font: .title),
    NamedFont(name: "Headline", font: .headline),
    NamedFont(name: "Body", font: .body),
    NamedFont(name: "Caption", font: .caption)
]

var body: some View {
    ForEach(namedFonts) { namedFont in
        Text(namedFont.name)
            .font(namedFont.font)
    }
}
```

![A vertically arranged stack of labels showing various standard fonts,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-ForEach-fonts@2x.png)

Some containers like [`List`](./list.md) or [`LazyVStack`](./lazyvstack.md) will query the elements within a for each lazily. To obtain maximal performance, ensure that the view created from each element in the collection represents a constant number of views.

For example, the following view uses an if statement which means each element of the collection can represent either 1 or 0 views, a non-constant number.

```swift
ForEach(namedFonts) { namedFont in
    if namedFont.name.count != 2 {
        Text(namedFont.name)
    }
}
```

You can make the above view represent a constant number of views by wrapping the condition in a [`VStack`](./vstack.md), an [`HStack`](./hstack.md), or a [`ZStack`](./zstack.md).

```swift
ForEach(namedFonts) { namedFont in
    VStack {
        if namedFont.name.count != 2 {
            Text(namedFont.name)
        }
    }
}
```

When enabling the following launch argument, SwiftUI will log when it encounters a view that produces a non-constant number of views in these containers:

```swift
-LogForEachSlowPath YES
```

## Topics

### Creating a collection
- [init(Data)](./foreach/init%28_%29.md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](./foreach/init%28_,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](./foreach/init%28_,id,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](./foreach/init%28sections,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init<V>(subviews: V, content: (Subview) -> Content)](./foreach/init%28subviews,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.
### Creating an editable collection
- [init<C, R>(Binding<C>, editActions: EditActions<C>, content: (Binding<C.Element>) -> R)](./foreach/init%28_,editactions,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.
- [init<C, R>(Binding<C>, id: KeyPath<C.Element, ID>, editActions: EditActions<C>, content: (Binding<C.Element>) -> R)](./foreach/init%28_,id,editactions,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.
### Accessing content
- [var content: (Data.Element) -> Content](./foreach/content.md)
  A function to create content on demand using the underlying data.
- [var data: Data](./foreach/data.md)
  The collection of underlying identified data that SwiftUI uses to create views dynamically.

## Relationships

### Conforms To
- [AccessibilityRotorContent](./accessibilityrotorcontent.md)
- [AttachmentContent](../RealityKit/attachmentcontent.md)
- [Chart3DContent](../Charts/chart3dcontent.md)
- [ChartContent](../Charts/chartcontent.md)
- [Copyable](../Swift/copyable.md)
- [CustomizableToolbarContent](./customizabletoolbarcontent.md)
- [DynamicMapContent](../MapKit/dynamicmapcontent.md)
- [DynamicTableRowContent](./dynamictablerowcontent.md)
- [DynamicViewContent](./dynamicviewcontent.md)
- [Escapable](../Swift/escapable.md)
- [MapContent](../MapKit/mapcontent.md)
- [SceneAccessoryContent](./sceneaccessorycontent.md)
- [TabContent](./tabcontent.md)
- [TableRowContent](./tablerowcontent.md)
- [ToolbarContent](./toolbarcontent.md)
- [View](./view.md)

## See Also

### Iterating over dynamic data
- [struct ForEachSectionCollection](./foreachsectioncollection.md)
  A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [struct ForEachSubviewCollection](./foreachsubviewcollection.md)
  A collection which allows a view to be treated as a collection of its subviews in a for each loop.
- [protocol DynamicViewContent](./dynamicviewcontent.md)
  A type of view that generates views from an underlying collection of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach)*