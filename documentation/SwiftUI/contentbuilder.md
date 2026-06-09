# ContentBuilder

**Framework**: SwiftUI  
**Kind**: typealias

A custom parameter attribute that constructs views and other content types from closures.

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
typealias ContentBuilder = ViewBuilder
```

#### Discussion

You apply `ContentBuilder`, a type alias for [`ViewBuilder`](viewbuilder.md), as a parameter attribute to closure parameters, computed properties, or protocol requirements. Then, SwiftUI builds content from multiple statements in the closures you provide. For example, the following `contextMenu` function accepts a closure that produces one or more views from the content builder.

```swift
func contextMenu<MenuItems: View>(
    @ContentBuilder menuItems: () -> MenuItems
) -> some View
```

You can use multiple-statement closures to provide several subviews, as the following example shows:

```swift
myView.contextMenu {
    Text("Cut")
    Text("Copy")
    Text("Paste")
    if isSymbol {
        Text("Jump to Definition")
    }
}
```

You can also use `ContentBuilder` with other SwiftUI-style result builders. For example, the following computed property iterates over cases in an enumeration to produce toolbar items.

```swift
@ContentBuilder
var editingToolbarItems: some ToolbarContent {
    ForEach(EditingOptions.toolbarItems, id: \.self) { editingOption in
        ToolbarItem {
            Button(editingOption.title) {
                editingOption.action()
            }
        }
    }
}
```

SwiftUI constructs type-agnostic content from closures that you mark with `ContentBuilder`, which serves as the unified replacement for type-specific builders like [`ToolbarContentBuilder`](toolbarcontentbuilder.md) and [`CommandsBuilder`](commandsbuilder.md).

In its build functions, `ContentBuilder` doesn’t enforce protocol conformance. Instead, it maintains type safety through conditional conformances on the content types it produces. For example, [`TupleContent`](tuplecontent.md) conditionally conforms to content types based on which types the content items it contains conform to. This allows a single, shared set of initializers on [`Group`](group.md), [`ForEach`](foreach.md), and [`Section`](section.md) to serve all content types, rather than a separate overloaded initializer per builder.

## See Also

- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [Wishlist: Planning travel in a SwiftUI app](wishlist-planning-travel-in-a-swiftui-app.md)
  Build a travel planning app that organizes trips into collections and tracks activity completion.
- [protocol View](view.md)
  A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [struct ViewBuilder](viewbuilder.md)
  A custom parameter attribute that constructs views from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentbuilder)*