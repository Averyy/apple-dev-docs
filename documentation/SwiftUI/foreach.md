# ForEach

**Framework**: SwiftUI  
**Kind**: struct

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

- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)

#### Overview

Use `ForEach` to provide views based on a [`RandomAccessCollection`](https://developer.apple.com/documentation/Swift/RandomAccessCollection) of some data type. Either the collection’s elements must conform to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) or you need to provide an `id` parameter to the `ForEach` initializer.

The following example creates a `NamedFont` type that conforms to [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable), and an array of this type called `namedFonts`. A `ForEach` instance iterates over the array, producing new [`Text`](text.md) instances that display examples of each SwiftUI [`Font`](font.md) style provided in the array.

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

![A vertically arranged stack of labels showing various standard fonts,](https://docs-assets.developer.apple.com/published/9819873f850b2cba7a4174a869ad369f/SwiftUI-ForEach-fonts%402x.png)

Some containers like [`List`](list.md) or [`LazyVStack`](lazyvstack.md) will query the elements within a for each lazily. To obtain maximal performance, ensure that the view created from each element in the collection represents a constant number of views.

For example, the following view uses an if statement which means each element of the collection can represent either 1 or 0 views, a non-constant number.

```swift
ForEach(namedFonts) { namedFont in
    if namedFont.name.count != 2 {
        Text(namedFont.name)
    }
}
```

You can make the above view represent a constant number of views by wrapping the condition in a [`VStack`](vstack.md), an [`HStack`](hstack.md), or a [`ZStack`](zstack.md).

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
- [init(Data)](foreach/init(_:).md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](foreach/init(_:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](foreach/init(_:id:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
### Creating an editable collection
- [init<C, R>(Binding<C>, editActions: EditActions<C>, content: (Binding<C.Element>) -> R)](foreach/init(_:editactions:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.
- [init<C, R>(Binding<C>, id: KeyPath<C.Element, ID>, editActions: EditActions<C>, content: (Binding<C.Element>) -> R)](foreach/init(_:id:editactions:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.
### Accessing content
- [var content: (Data.Element) -> Content](foreach/content.md)
  A function to create content on demand using the underlying data.
- [var data: Data](foreach/data.md)
  The collection of underlying identified data that SwiftUI uses to create views dynamically.
### Initializers
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](foreach/init(sections:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init<V>(subviews: V, content: (Subview) -> Content)](foreach/init(subviews:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

## Relationships

### Conforms To
- [AccessibilityRotorContent](accessibilityrotorcontent.md)
- [AttachmentContent](../RealityKit/AttachmentContent.md)
- [Chart3DContent](../Charts/Chart3DContent.md)
- [ChartContent](../Charts/ChartContent.md)
- [Copyable](../Swift/Copyable.md)
- [DynamicMapContent](../MapKit/DynamicMapContent.md)
- [DynamicTableRowContent](dynamictablerowcontent.md)
- [DynamicViewContent](dynamicviewcontent.md)
- [MapContent](../MapKit/MapContent.md)
- [TabContent](tabcontent.md)
- [TableRowContent](tablerowcontent.md)
- [View](view.md)

## See Also

- [struct ForEachSectionCollection](foreachsectioncollection.md)
  A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [struct ForEachSubviewCollection](foreachsubviewcollection.md)
  A collection which allows a view to be treated as a collection of its subviews in a for each loop.
- [protocol DynamicViewContent](dynamicviewcontent.md)
  A type of view that generates views from an underlying collection of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach)*