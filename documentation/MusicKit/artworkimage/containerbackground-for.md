# containerBackground(_:for:)

**Framework**: MusicKit  
**Kind**: method

Sets the container background of the enclosing container using a view.

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
nonisolated
func containerBackground<S>(_ style: S, for container: ContainerBackgroundPlacement) -> some View where S : ShapeStyle
```

#### Discussion

The following example uses a `LinearGradient` as a background:

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Blue") {
                    Text("Blue")
                    .containerBackground(.blue.gradient, for: .navigation)
                }
                NavigationLink("Red") {
                    Text("Red")
                    .containerBackground(.red.gradient, for: .navigation)
                }
            }
        }
    }
}
```

The `.containerBackground(_:for:)` modifier differs from the `View/background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an entire parent container. `ContainerBackgroundPlacement` describes the available containers.

- Parameters - style: The shape style to use as the container background.
- container: The container that will use the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/containerbackground(_:for:))*