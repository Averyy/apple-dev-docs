# matchedTransitionSource(id:in:)

**Framework**: SwiftUI  
**Kind**: method

Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
nonisolated
func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some ToolbarContent
```

#### Discussion

Use this modifier in conjunction with `View.navigationTransition(_:)` to provide a source for the transition effect:

```swift
struct ContentView: View {
    @State private var isPresented = false
    @Namespace private var namespace

    var body: some View {
        NavigationStack {
            DetailView()
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        Button("Show Sheet", systemImage: "globe") {
                            isPresented = true
                        }
                    }
                    .matchedTransitionSource(
                        id: "world", in: namespace)
                }
                .sheet(isPresented: $isPresented) {
                    SheetView()
                        .navigationTransition(
                            .zoom(sourceID: "world", in: namespace))
                }
        }
    }
}
```

## Parameters

- `id`: The identifier, often derived from the identifier of   the data being displayed by the toolbar content.
- `namespace`: The namespace in which defines the  . New   namespaces are created by adding an   variable   to a   or ``ToolbarContent` type and reading its value in   the type’s body method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/matchedtransitionsource(id:in:))*