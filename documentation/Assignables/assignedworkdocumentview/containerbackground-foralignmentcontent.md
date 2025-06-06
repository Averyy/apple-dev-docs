# containerBackground(for:alignment:content:)

**Framework**: Assignables  
**Kind**: method

Sets the container background of the enclosing container using a view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func containerBackground<V>(for container: ContainerBackgroundPlacement, alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Discussion

The following example uses a custom `View` as a background:

```None
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Image") {
                    Text("Image")
                    .containerBackground(for: .navigation) {
                        Image(name: "ImageAsset")
                    }
                }
            }
        }
    }
}
```

The `.containerBackground(for:alignment:content:)` modifier differs from the `View/background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an entire parent container. `ContainerBackgroundPlacement` describes the available containers.

## Parameters

- `alignment`: The alignment that the modifier uses to position the   implicit   that groups the background views. The default is   .
- `container`: The container that will use the background.
- `content`: The view to use as the background of the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/containerbackground(for:alignment:content:))*