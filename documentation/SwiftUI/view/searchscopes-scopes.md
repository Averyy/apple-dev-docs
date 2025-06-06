# searchScopes(_:scopes:)

**Framework**: SwiftUI  
**Kind**: method

Configures the search scopes for this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchScopes<V, S>(_ scope: Binding<V>, @ViewBuilder scopes: () -> S) -> some View where V : Hashable, S : View
```

## Mentions

- [Scoping a search operation](scoping-a-search-operation.md)

#### Discussion

To enable people to narrow the scope of their searches, you can create a type that represents the possible scopes, and then create a state variable to hold the current selection. For example, you can scope the product search to just fruits or just vegetables:

```swift
enum ProductScope {
    case fruit
    case vegetable
}

@State private var scope: ProductScope = .fruit
```

Provide a binding to the scope, as well as a view that represents each scope:

```swift
ProductList()
    .searchable(text: $text, tokens: $tokens) { token in
        switch token {
        case .apple: Text("Apple")
        case .pear: Text("Pear")
        case .banana: Text("Banana")
        }
    }
    .searchScopes($scope) {
        Text("Fruit").tag(ProductScope.fruit)
        Text("Vegetable").tag(ProductScope.vegetable)
    }
```

SwiftUI uses this binding and view to add a [`Picker`](picker.md) with the search field. In iOS, iPadOS, macOS, and tvOS, the picker appears below the search field when search is active. To ensure that the picker operates correctly, match the type of the scope binding with the type of each view’s tag. Then modify your search to account for the current value of the `scope` state property.

For more information about using searchable modifiers, see [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md).

## Parameters

- `scope`: The active scope of the search field.
- `scopes`: A view builder that represents the scoping options   SwiftUI uses to populate a  .

## See Also

- [Scoping a search operation](scoping-a-search-operation.md)
  Divide the search space into a few broad categories.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](view/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [struct SearchScopeActivation](searchscopeactivation.md)
  The ways that searchable modifiers can show or hide search scopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchscopes(_:scopes:))*