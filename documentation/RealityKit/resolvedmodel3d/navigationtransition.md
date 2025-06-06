# navigationTransition(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the navigation transition style for this view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func navigationTransition(_ style: some NavigationTransition) -> some View
```

#### Discussion

Add this modifier to a view that appears within a `NavigationStack` or a sheet, outside of any containers such as `VStack`.

```None
struct ContentView: View {
    @Namespace private var namespace
    var body: some View {
        NavigationStack {
            NavigationLink {
                DetailView()
                    .navigationTransition(.zoom(sourceID: "world", in: namespace))
            } label: {
                Image(systemName: "globe")
                    .matchedTransitionSource(id: "world", in: namespace)
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/navigationtransition(_:))*