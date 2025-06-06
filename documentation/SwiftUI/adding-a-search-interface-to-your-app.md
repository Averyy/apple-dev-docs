# Adding a search interface to your app

**Framework**: SwiftUI

Present an interface that people can use to search for content in your app.

#### Overview

Add a search interface to your app by applying one of the searchable view modifiers — like [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md) — to a [`NavigationSplitView`](navigationsplitview.md) or [`NavigationStack`](navigationstack.md), or to a view inside one of these. A search field then appears in the toolbar. The precise placement and appearance of the search field depends on the platform, where you put the modifier in code, and its configuration.

![A wide rectangle with rounded corners that contains a magnifying glass on the left, followed by the text Search in a gray color.](https://docs-assets.developer.apple.com/published/f52e89b1ae79d7dcf829d6201267252b/Search-add-0-macOS%402x.png)

The searchable modifier that creates the field takes a [`Binding`](binding.md) to a string that represents the search field’s text. You provide the storage for the string — and optionally for an array of discrete search tokens — that you use to conduct the search. To learn about managing the search field’s data, see [`Performing a search operation`](performing-a-search-operation.md).

##### Place the Search Field Automatically

You can automatically place the search field by adding the [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md) modifier to a navigation element like a navigation split view:

```swift
struct ContentView: View {
    @State private var departmentId: Department.ID?
    @State private var productId: Product.ID?
    @State private var searchText: String = ""

    var body: some View {
        NavigationSplitView {
            DepartmentList(departmentId: $departmentId)
        } content: {
            ProductList(departmentId: departmentId, productId: $productId)
        } detail: {
            ProductDetails(productId: productId)
        }
        .searchable(text: $searchText) // Adds a search field.
    }
}
```

With this configuration, the search field appears on the trailing edge of the toolbar in macOS. In iOS and iPadOS, the first or second column displays the search field in a double or triple column navigation view, respectively. The above three-column example puts the search field at the top of the middle column on iPad.

##### Control the Placement Structurally

To add a search field to a specific column in iOS and iPadOS, add the searchable modifier to a view in that column. For example, to indicate that the search covers departments in the previous example, you could place the search field in the first column by adding the modifier to that column’s `DepartmentList` view instead of to the navigation split view:

```swift
NavigationSplitView {
    DepartmentList(departmentId: $departmentId)
        .searchable(text: $searchText)
} content: {
    ProductList(departmentId: departmentId, productId: $productId)
} detail: {
    ProductDetails(productId: productId)
}
```

![An iPad screen with three navigation panes. The pane on the left lists the items, Produce, Frozen, and Bakery under the title, Department. The middle pane has the placeholder text, Select a Department under the title, Product. The pane on the right has the placeholder text, Select a Product. The toolbar of the left-most pane has a search field just below the title that displays the placeholder text, Search.](https://docs-assets.developer.apple.com/published/8db18db9c632f695504a7fa566f117aa/Search-add-2-iPadOS%402x.png)

##### Control the Placement Programmatically

You can alternatively use the `placement` input parameter to suggest a [`SearchFieldPlacement`](searchfieldplacement.md) value for the search interface. For example, you can achieve the same results as the previous example in macOS using the [`sidebar`](searchfieldplacement/sidebar.md) placement:

```swift
NavigationSplitView {
    DepartmentList(departmentId: $departmentId)
} content: {
    ProductList(departmentId: departmentId, productId: $productId)
} detail: {
    ProductDetails(productId: productId)
}
.searchable(text: $searchText, placement: .sidebar)
```

![A macOS window with three navigation panes. The pane on the left lists the items, Produce, Frozen, and Bakery. The middle pane has the placeholder text, Select a Department. The pane on the right has the placeholder text, Select a Product. The left-most pane has a search field above the list of items that has the placeholder text, Search.](https://docs-assets.developer.apple.com/published/10ce7a28b40a9710b1bd821108e702c8/Search-add-3-macOS%402x.png)

If SwiftUI can’t satisfy the placement request, like when you ask for sidebar placement in a searchable modifier that isn’t applied to a navigation split view, SwiftUI relies instead on its automatic placement rules.

##### Set a Prompt for the Search Field

By default, the search field contains Search as the placeholder text, to prompt people on how to use the field. You can customize the prompt by setting either a string, a [`Text`](text.md) view, or a [`LocalizedStringKey`](localizedstringkey.md) for the searchable modifier’s `prompt` input parameter. For example, you might use this to clarify that the search field in the Department column searches among both departments and the products in each department:

```swift
DepartmentList(departmentId: $departmentId)
    .searchable(text: $searchText, prompt: "Departments and products")
```

![A screenshot that shows the text, Department in title font at the top, a search field below the title, and three items listed below the search field called, Produce, Frozen, and Bakery. The search field has the placeholder text, Departments and products.](https://docs-assets.developer.apple.com/published/2d3c92d15a0de2b73ffcfbcc2b45005f/Search-add-4-iPadOS%402x.png)

## See Also

- [Performing a search operation](performing-a-search-operation.md)
  Update search results based on search text and optional tokens that you store.
- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:tokens:placement:prompt:token:)](view/searchable(text:tokens:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens.
- [func searchable(text:editableTokens:placement:prompt:token:)](view/searchable(text:editabletokens:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [struct SearchFieldPlacement](searchfieldplacement.md)
  The placement of a search field in a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app)*